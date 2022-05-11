python benchmark --warmup True --cuda_sync True --cuda_time True
python benchmark --warmup True --cuda_sync False --cuda_time True
python benchmark --warmup True --cuda_sync True --cuda_time False
python benchmark --warmup True --cuda_sync False --cuda_time False

python benchmark --warmup False --cuda_sync True --cuda_time True
python benchmark --warmup False --cuda_sync False --cuda_time True
python benchmark --warmup False --cuda_sync True --cuda_time False
python benchmark --warmup False --cuda_sync False --cuda_time False
