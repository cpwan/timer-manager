# TimerManager
Time a script multiple times.

**Installation**
```shell
python -m pip install "TimerManager @ git+https://github.com/cpwan/timer-manager.git"
```

```python
from TimerManager import TimerManager

timer = TimerManager.get('My timer')
for i in range(10):
    with timer:
        i=0
        while(i<10000):
            i+=1
timer
# [10 runs] Total 0.0217s	 Mean 0.0022s	 Min 0.0020s	 Max 0.0026s	 
#--- upon module exit --- 
# {'My timer': [10 runs] Total 0.0269s     Mean 0.0027s    Min 0.0025s     Max 0.0029s     }
```
