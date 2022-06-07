import argparse
import time
from ast import arg
from typing import Tuple

import numpy as np
import torch
import torchvision.models as models


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


parser = argparse.ArgumentParser(description="PyTorch benchmark example")
parser.add_argument(
    "--warmup",
    type=str2bool,
    default=True,
    help="If you set this value to true, GPU warmup process is started.",
)
parser.add_argument(
    "--cuda_sync", type=str2bool, default=True, help="Cuda sync on(True) / off(False).",
)
parser.add_argument(
    "--cuda_time",
    type=str2bool,
    default=True,
    help="CUDA Timer on(True) / off(False).",
)
args = parser.parse_args()


def benchmark(
    model: torch.nn.Module,
    device: str,
    input_shape: Tuple[int, int, int, int] = (1, 3, 224, 224),
    nwarmup: int = 50,
    nruns: int = 1000,
):
    """Benchmark module."""
    input_data = torch.randn(input_shape)
    input_data = input_data.to(device)
    with torch.no_grad():
        if args.warmup:
            for _ in range(nwarmup):
                features = model(input_data)

    if args.cuda_sync:
        torch.cuda.synchronize()
    timings = []
    with torch.no_grad():
        for i in range(1, nruns + 1):
            if args.cuda_time:
                start_time, end_time = (
                    torch.cuda.Event(enable_timing=True),
                    torch.cuda.Event(enable_timing=True),
                )
                start_time.record()
            else:
                start_time = time.time()
            features = model(input_data)
            if args.cuda_time:
                end_time.record()
            if args.cuda_sync:
                torch.cuda.synchronize()

            if args.cuda_time:
                curr_time = start_time.elapsed_time(end_time) / 1000
            else:
                end_time = time.time()
                curr_time = end_time - start_time

            timings.append(curr_time)

    print("Average time: %.2f ms" % (np.mean(timings) * 1000))


def main():
    """Main fucntion.
    This function will be set benchmark preparation thing.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    resnet50 = models.resnet50(pretrained=True)
    resnet50.eval().to(device)
    print(f"warmup {args.warmup} cuda sync {args.cuda_sync} cuda time {args.cuda_time}")
    benchmark(model=resnet50, device=device)

    return


if __name__ == "__main__":
    main()
