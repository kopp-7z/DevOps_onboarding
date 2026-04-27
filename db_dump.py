import subprocess
import gzip
import shutil

def dump_db():
    dump_file = "wikijs_dump.sql"
    zipped_file = "wikijs_dump.sql.gz"

    with open(dump_file, "w") as f:
        subprocess.run(
            ["docker", "exec", "onboarding-db-1", "pg_dump", "-U", "user", "-d", "wikijs"],
            stdout=f,
            check=True
        )

    with open(dump_file, "rb") as f_in, gzip.open(zipped_file, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

if __name__ == "__main__":
    dump_db()
