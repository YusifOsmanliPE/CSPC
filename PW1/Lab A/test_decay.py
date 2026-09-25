import numpy as np
import pytest
from decay import simulate, simulate_loop
def test_starts_at_N0():
    assert simulate(1000, 0.4)[0] == 1000

def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.1)

def test_matches_law():
    N0 = 1000
    lam = 0.4
    t = 5
    dt = 0.05
    steps = int(t / dt)

    results = []
    for seed in range(50):
        res = simulate(N0, lam, dt=dt, steps=steps, seed=seed)
        results.append(res[-1])

    avg_remaining = np.mean(results)
    expected = N0 * np.exp(-lam * t)

    assert expected == pytest.approx(avg_remaining, rel=0.05)