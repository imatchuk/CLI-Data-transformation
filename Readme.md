Status ci 
<img src="https://github.com/imatchuk/CLI-Data-transformation/workflows/My-Otus-lesson-ci/badge.svg?branch=master">


Формат экспортера
________________________________________________________________________
Метрики
________________________________________________________________________
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 648.0
python_gc_objects_collected_total{generation="1"} 342.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 135.0
python_gc_collections_total{generation="1"} 12.0
python_gc_collections_total{generation="2"} 1.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="11",patchlevel="0",version="3.11.0"} 1.0
# HELP flask_exporter_info Information about the Prometheus Flask exporter
# TYPE flask_exporter_info gauge
flask_exporter_info{version="0.21.0"} 1.0
# HELP flask_http_request_duration_seconds Flask HTTP request duration in seconds
# TYPE flask_http_request_duration_seconds histogram
flask_http_request_duration_seconds_bucket{le="0.005",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="0.01",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="0.025",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="0.05",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="0.075",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="0.1",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="0.25",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="0.5",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="0.75",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="1.0",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="2.5",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="5.0",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="7.5",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="10.0",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_count{method="GET",path="/favicon.ico",status="404"} 1.0
flask_http_request_duration_seconds_sum{method="GET",path="/favicon.ico",status="404"} 0.000404000049456954
flask_http_request_duration_seconds_bucket{le="0.005",method="GET",path="/",status="200"} 4.0
flask_http_request_duration_seconds_bucket{le="0.01",method="GET",path="/",status="200"} 7.0
flask_http_request_duration_seconds_bucket{le="0.025",method="GET",path="/",status="200"} 7.0
flask_http_request_duration_seconds_bucket{le="0.05",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.075",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.1",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.25",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.5",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.75",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="1.0",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="2.5",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="5.0",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="7.5",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="10.0",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_count{method="GET",path="/",status="200"} 8.0
flask_http_request_duration_seconds_sum{method="GET",path="/",status="200"} 0.05080720013938844
flask_http_request_duration_seconds_bucket{le="0.005",method="POST",path="/add",status="302"} 0.0
flask_http_request_duration_seconds_bucket{le="0.01",method="POST",path="/add",status="302"} 1.0
flask_http_request_duration_seconds_bucket{le="0.025",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.05",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.075",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.1",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.25",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.5",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.75",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="1.0",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="2.5",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="5.0",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="7.5",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="10.0",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="+Inf",method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_count{method="POST",path="/add",status="302"} 3.0
flask_http_request_duration_seconds_sum{method="POST",path="/add",status="302"} 0.03085420001298189
flask_http_request_duration_seconds_bucket{le="0.005",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.01",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.025",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.05",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.075",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.1",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.25",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.5",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="0.75",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="1.0",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="2.5",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="5.0",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="7.5",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="10.0",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_bucket{le="+Inf",method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_count{method="POST",path="/update",status="302"} 3.0
flask_http_request_duration_seconds_sum{method="POST",path="/update",status="302"} 0.0006679000798612833
# HELP flask_http_request_duration_seconds_created Flask HTTP request duration in seconds
# TYPE flask_http_request_duration_seconds_created gauge
flask_http_request_duration_seconds_created{method="GET",path="/favicon.ico",status="404"} 1.669143661645355e+09
flask_http_request_duration_seconds_created{method="GET",path="/",status="200"} 1.6691444352550473e+09
flask_http_request_duration_seconds_created{method="POST",path="/add",status="302"} 1.6691444410225582e+09
flask_http_request_duration_seconds_created{method="POST",path="/update",status="302"} 1.6691450860266793e+09
# HELP flask_http_request_total Total number of HTTP requests
# TYPE flask_http_request_total counter
flask_http_request_total{method="GET",status="404"} 1.0
flask_http_request_total{method="GET",status="200"} 8.0
flask_http_request_total{method="POST",status="302"} 6.0
# HELP flask_http_request_created Total number of HTTP requests
# TYPE flask_http_request_created gauge
flask_http_request_created{method="GET",status="404"} 1.669143661645355e+09
flask_http_request_created{method="GET",status="200"} 1.6691444352550473e+09
flask_http_request_created{method="POST",status="302"} 1.6691444410225582e+09
# HELP flask_http_request_exceptions_total Total number of HTTP requests which resulted in an exception
# TYPE flask_http_request_exceptions_total counter
