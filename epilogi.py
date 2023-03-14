s=0
syn_bohth=0
for i in range(5):
    onoma=raw_input("Dwse onoma: ")
    dendra=int(input("Dwse arithmo dendron: "))
    if dendra<=50:
        syn=dendra*45
        syn_bohth=syn_bohth+syn
        print onoma," Poso bohthias: ",syn
    elif dendra<=120:
        syn=50*45+(dendra*60)
        syn_bohth=syn_bohth+syn
        print onoma," Poso bohthias: ",syn
        if syn>=5000:
            s+=1
    else:
        syn=50*45+(120*60)+(dendra*80)
        syn_bohth=syn_bohth+syn
        print onoma," Poso bohthias: ",syn
        if syn>=5000:
            s+=1
print "Synoliki oikonomiki bohthia: ",syn_bohth
print "Plithos pou peiran panw apo 5.000: ",s
