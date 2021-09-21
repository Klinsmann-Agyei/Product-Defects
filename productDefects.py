import scipy.stats as stats
import numpy as np

lam = 7
print(stats.poisson.pmf(lam, lam))
print(stats.poisson.cdf(4, lam))
print(1 - stats.poisson.cdf(9, lam))

year_defects = stats.poisson.rvs(lam, size = 356)
print(year_defects[0:20])
print(lam*365)
print(sum(year_defects))
print(np.mean(year_defects))
print(year_defects.max())
1 - stats.poisson.cdf(year_defects.max(), lam)

print(stats.poisson.ppf(0.9, lam))
print(sum(year_defects > stats.poisson.ppf(0.9, lam))/len(year_defects))
