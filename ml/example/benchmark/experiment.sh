python benchmark.py --warmup False --cuda_sync True --cuda_time True
python benchmark.py --warmup False --cuda_sync False --cuda_time True
python benchmark.py --warmup False --cuda_sync True --cuda_time False
python benchmark.py --warmup False --cuda_sync False --cuda_time False

python benchmark.py --warmup True --cuda_sync True --cuda_time True
python benchmark.py --warmup True --cuda_sync False --cuda_time True
python benchmark.py --warmup True --cuda_sync True --cuda_time False
python benchmark.py --warmup True --cuda_sync False --cuda_time False
