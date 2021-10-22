#    Copyright [2021] [Ching Pui WAN]

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import time
class Timer:
    def __init__(self):
        self.accum =0.0
        self.n = 0
        self.last_tic=None
        self.min_,self.max_=None,None
    
    def tic(self):
        self.last_tic=time.perf_counter()
        
    def toc(self):
        self.last_toc=time.perf_counter()
        if self.last_tic==None:
            raise 'The timer has not started yet.'
        self.update()
        
    def update(self):
        elapsed=self.last_toc-self.last_tic
        self.last_toc=None
        self.last_tic=None
        
        self.n+=1
        self.accum+=elapsed
        if not self.min_ or elapsed<self.min_:
            self.min_=elapsed
        if not self.max_ or elapsed>self.max_:
            self.max_=elapsed            
        
    def __enter__(self):
        self.tic()
    def __exit__(self,*exc):
        self.toc()
    def __repr__(self):
        if self.n==0:
            return f'The timer has not started yet.'
        mean_=self.accum/self.n
        return f'[{self.n} runs] Total {self.accum:.4f}s\t Mean {mean_:.4f}s\t Min {self.min_:.4f}s\t Max {self.max_:.4f}s\t '

class TimerManager:
    timers=dict()
    @staticmethod
    def get(name):
        item=TimerManager.timers.setdefault(name,Timer())
        return item
    @staticmethod
    def reset():
        TimerManager.timers=dict()
    @staticmethod
    def print():
        return print(TimerManager.timers)


import atexit
atexit.register(TimerManager.print)
