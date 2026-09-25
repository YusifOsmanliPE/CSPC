# CSPC - Computer Science for Physics and Chemistry
# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW1/Lab\ A/environment.yml
conda activate cspc

## PW1
Lab A: Reproducible Foundations

**What I built:**
Set up version control, conda environment, automated pytest suite, and vectorised simulation comparison.

**Speed comparison (loop vs NumPy):**
- loop: 4.2210 s
- numpy: 0.0004 s
- speed-up: 9945.7x faster

**Tests:** all passing? yes

**Conclusion:**
Using NumPy's vectorised operations significantly reduced execution time compared to standard Python loops. All pytest test cases passed successfully.