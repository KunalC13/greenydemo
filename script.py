from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

# Sample CPU-heavy task (Fibonacci)
def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

fib(28)

emissions = tracker.stop()
print(f"Emissions: {emissions} kg CO₂")
