import pandas as pd
import numpy_financial as npf
import numpy as np
"""
i = 0.16
print(-9364 + 10000 / (1 + i) + 1000 / ((1 + i) ** 2))
i = 0.1
print(-9364 + 10000 / (1 + i) + 1000 / ((1 + i) ** 2))
i = 0.2
print(-9364 + 10000 / (1 + i) + 1000 / ((1 + i) ** 2))
"""
from typing import List, Optional
from scipy.optimize import fsolve
class Cashflow:
    def __init__(self,
                 amount: float,
                 t: int):
        self.amount = amount
        self.t = t
    def present_value(self, r: float) -> 'Cashflow':
        return Cashflow(amount=self.amount * (1 + r) ** (-self.t), t=0)
def npv(rate: float, cfs: List[Cashflow]) -> float:
    return sum(map(lambda cf: cf.present_value(rate).amount, cfs))
def irr(cfs: List[Cashflow]) -> Optional[float]:
    result = fsolve(npv, x0=0.15, args=(cfs,))
    return result[0] if result else None

def geometric(a,i,n):
    r = 1 + i
    return a * (1 - r ** (n + 1)) / (1 - r)
class Amortization:
    def __init__(self, amount: float, rate: float, t: int):
        self.amount = amount
        self.rate = rate
        self.t = t    @property
    def payment_amount(self) -> float:
        return self.amount * self.rate / (1 - (1 + self.rate) ** -self.t)
    def to_dataframe(self, default_prob: float) -> pd.DataFrame:
        times = list(range(0, self.t + 1))
        payments = [0]+[self.payment_amount for _ in range(self.t)]
        balances = [self.amount]
        interests = [0]
        principals = [0]
        cashflows = [-self.amount]
        irr = [0]
        pds=[default_prob]

        for _ in times[1:]:
            interest = balances[-1]*self.rate
            balances.append(balances[-1]-self.payment_amount+interest)
            interests.append(balances[-1]*self.rate)
            principals.append(self.payment_amount-interests[-1])
            cashflows.append(self.payment_amount)
            irr.append(npf.irr(cashflows))
            pds.append((default_prob)*(1-pds[-1]))
        pds[-1]=(1-default_prob)**self.t
        expected_irr = np.array(pds)*np.array(irr)
        ead=np.array(balances)*np.array(pds)
        e_irr = np.array(pds) @ np.array(irr)
        df = pd.DataFrame({"T":times,
                             "Balance":balances,
                             "Payment": payments,
                             "Interest": interests,
                             "Principal":principals,
                             "Cashflows":cashflows,
                             "Tir":irr,
                             "PD":pds,
                             "Expected IRR":expected_irr,
                             "EAD": ead})        #df.to_html()
        return df