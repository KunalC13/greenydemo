from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

fib(30)

emissions = tracker.stop()
print(f"Emissions: {emissions} kg CO₂")
