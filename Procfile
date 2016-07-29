web: pip install -e . --process-dependency-links && recast-frontend-admin mk_config -o herokuconf.yaml && recast-frontend server --config herokuconf.yaml
worker: pip install -e . --process-dependency-links && recast-frontend-admin mk_config -o herokuconf.yaml && recast-frontend celery --config herokuconf.yaml
