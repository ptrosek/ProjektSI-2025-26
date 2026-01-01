from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd

class SignalStrategy(Strategy):
    """
    Strategy that trades based on pre-calculated signals.
    Implements rebalancing logic.
    """
    rebalance_freq = 'daily' # 'daily', 'weekly', 'monthly'
    
    def init(self):
        # We assume self.data contains the 'Signal' column.
        pass

    def next(self):
        # Current date/time index
        current_time = self.data.index[-1]
        
        # Check if we should rebalance
        should_rebalance = False
        
        # Logic to determine if we are in a new period
        # We need to look at the *previous* bar's time to detect a change.
        if len(self.data.index) > 1:
            prev_time = self.data.index[-2]
        else:
            prev_time = None

        if self.rebalance_freq == 'daily':
            should_rebalance = True
            
        elif self.rebalance_freq == 'weekly':
            # Check if week number changed or it's a Monday
            # Robust: If prev_time is None (first bar), rebalance.
            # Else if current week != prev week
            if prev_time is None:
                should_rebalance = True
            else:
                # isocalendar returns (year, week, day)
                if current_time.isocalendar()[1] != prev_time.isocalendar()[1]:
                    should_rebalance = True
                    
        elif self.rebalance_freq == 'monthly':
            # Check if month changed
            if prev_time is None:
                should_rebalance = True
            else:
                if current_time.month != prev_time.month:
                    should_rebalance = True
        
        # Access signal (1: Buy, -1: Sell, 0: Neutral)
        # The signal was generated on the previous close (at 'prev_time') to be executed now.
        # But wait, backtesting.py executes orders *on the next bar* if we place them now?
        # No, self.buy() places an order for the *next* open.
        # However, our signal series is aligned such that `Signal[i]` is the decision made at close of `i`.
        # So in `next()` (which is essentially close of `i`), we look at `Signal[-1]` (Signal[i]) to trade at `Open[i+1]`.
        
        signal = self.data.Signal[-1]
        
        # Logic: If it is a rebalancing day (start of new period), we execute the signal.
        # If it's NOT a rebalancing day:
        # - "Daily": we check every day (always true).
        # - "Weekly": We only act if the week just changed.
        
        if not should_rebalance:
            return

        # Execution Logic
        if signal == 1:
            if not self.position.is_long:
                self.buy(size=0.95)
        elif signal == 0:
            # Exit if neutral
            if self.position:
                self.position.close()
