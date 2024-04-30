def create_miners():
    for i in range(1, 100 + 1):
        with open(f'solo_miner{i}.py', 'w') as f:
            f.write(f'''
import solo_miner_base
import nounces

solo_miner_base.START_NONCE = nounces.start{i}
solo_miner_base.END_NONCE = nounces.end{i}
solo_miner_base.LOG_NAME = 'logs/solo_miner{i}.log'

solo_miner_base.run()
    ''')


def run_all_miners():
    import subprocess
    import os
    import time

    # Get the current working directory
    directory = os.getcwd()

    # Iterate through each script in the directory
    for filename in os.listdir(directory):
        if filename.startswith("solo_miner") and filename.endswith(".py") and filename != "solo_miner_base.py":
            # Construct the full path to the script
            script_path = os.path.join(directory, filename)

            # Run the script in a non-blocking manner using subprocess
            subprocess.Popen(["py", script_path])
        time.sleep(1)


def run_n_miners(n):
    import subprocess
    import os
    import time

    # Get the current working directory
    directory = os.getcwd()

    # Iterate through each script in the directory
    for filename in os.listdir(directory):
        if filename.startswith("solo_miner") and filename.endswith(".py") and filename != "solo_miner_base.py":
            # Construct the full path to the script
            script_path = os.path.join(directory, filename)

            # Run the script in a non-blocking manner using subprocess
            subprocess.Popen(["py", script_path])
            n -= 1
        if n == 0:
            break
        time.sleep(1)


def delete_all_logs():
    import os

    # Get the current working directory
    directory = os.getcwd()
    # add logs to the directory
    directory = os.path.join(directory, "logs")

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.startswith("solo_miner") and filename.endswith(".log"):
            # Construct the full path to the log file
            log_path = os.path.join(directory, filename)

            # Delete the log file
            os.remove(log_path)


def generate_range(start_range, end_range, num_values, begin_index=1):
    step_size = (end_range - start_range + 1) // num_values

    for i in range(begin_index, num_values + begin_index):
        start_value = start_range + i * step_size
        end_value = start_range + (i + 1) * step_size - 1
        print(f"start{i} = {start_value}")
        print(f"end{i} = {end_value}")

def generate_range_fixed():
    start_range = 1000000000
    end_range = 49999999999

    num_values = 100
    step_size = (end_range - start_range + 1) // num_values

    for i in range(num_values):
        start_value = start_range + i * step_size
        end_value = start_range + (i + 1) * step_size - 1
        print(f"start{i + 1} = {start_value}")
        print(f"end{i + 1} = {end_value}")

# run_all_miners()
# run_n_miners(2)
# create_miners()


