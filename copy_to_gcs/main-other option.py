proc = subprocess.Popen(["gsutil", "-m", "rsync", "s3://input", "gs://output"])
try:
    outs, errs = proc.communicate(timeout=15)
    # now you can do something with the text in outs and errs
except TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()