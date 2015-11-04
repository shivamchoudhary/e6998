import views
def testing():
    india_counter = 0
    global_counter = 0
    attr = {'country':'indian'}
    for i in range(0,10000):
        if views.dry_run(attr)=="indian":
            india_counter+=1
        global_counter+=1
    print float(india_counter)/global_counter
testing() 
