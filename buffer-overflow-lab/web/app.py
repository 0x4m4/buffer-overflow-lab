from flask import Flask, request, render_template
import time
import sys
import os

app = Flask(__name__)

# Global variables to simulate resource exhaustion
memory_usage = []
request_count = 0
start_time = time.time()
CRASH_THRESHOLD = 5000  # Lower threshold for faster crash
MAX_REQUESTS = 20  # Lower max requests

@app.route('/', methods=['GET', 'POST'])
def vulnerable_function():
    global request_count, start_time, memory_usage
    buffer = [0] * 10

    if request.method == 'POST':
        request_count += 1
        user_input = request.form.get('input', '')
        
        try:
            # Super aggressive memory leak
            memory_usage.extend([1] * (len(user_input) * 100))
            
            # Heavy CPU usage simulation
            if len(user_input) > 20:
                time.sleep(2)  # Longer delay
            
            # More memory consumption
            temp_buffer = [ord(char) for char in user_input * 10]
            memory_usage.extend(temp_buffer)
            
            # Buffer overflow simulation
            for i, char in enumerate(user_input):
                buffer[i] = ord(char)
            
            # Immediate crash conditions
            if len(memory_usage) > CRASH_THRESHOLD:
                os._exit(1)  # Force immediate process termination
            
            if request_count > MAX_REQUESTS:
                os._exit(1)  # Force immediate process termination
            
            # Simulate memory corruption
            if len(user_input) > 50:
                os._exit(1)
            
            return f"Input processed: {''.join(map(chr, buffer))}"
            
        except IndexError:
            return "Buffer Overflow Detected!"
        except Exception as e:
            os._exit(1)  # Force immediate process termination
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
