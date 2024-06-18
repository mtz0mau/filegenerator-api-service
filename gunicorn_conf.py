import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:7321"
worker_class = "uvicorn.workers.UvicornWorker"
