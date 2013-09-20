import string
class funkcje:
    def par_gga(self,line):
        data=[]
        data=line.split(',')

        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        if data[3]=='N':
            latt=float(data[2][:2])+float(data[2][2:])/60
        elif data[3]=='S':
            latt=-1*float(data[2][:2])+float(data[2][2:])/60
        else:
            latt=''
        ind=string.find(data[4],".")
        if data[5]=='E':
            lonn=float(data[4][:(ind-2)])+float(data[4][(ind-2):])/60
        elif data[5]=='W':
            lonn=-1*float(data[4][:(ind-2)])+float(data[4][(ind-2):])/60
        else:
            lonn=''

        numsv=data[7]
        hdop=data[8]
        msl=data[9]
        geoid=data[11]
        fixstatus=data[6]
        query="""insert into nmeaGGA(utcgga,latgga,longga,fixstatus,numsv,hdop,msl,geoid) values('"""+str(utc)+"""',"""+str(latt)+""","""+str(lonn)+""","""+str(fixstatus)+""","""+str(numsv)+""","""+str(hdop)+""","""+str(msl)+""","""+str(geoid)+""");"""
        return query


    def par_rmc(self,line):
        data=[]
        data=line.split(',')

        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]

        if data[4]=='N':
            latt=float(data[3][:2])+float(data[3][2:])/60
        elif data[4]=="S":
            latt=-1*float(data[3][:2])+float(data[3][2:])/60
        else:
            latt=''
        ind=string.find(data[5],".")
        if data[6]=='E':
            lonn=float(data[5][:(ind-2)])+float(data[5][(ind-2):])/60
        elif data[6]=='W':
            lonn=-1*float(data[5][:(ind-2)])+float(data[5][(ind-2):])/60
        else:
            lonn=''

        speed=data[7]

        if data[2]=='A':    datastatus=1
        else:   datastatus=0

        query="""insert into nmeaRMC(utcrmc,latrmc,lonrmc,speed,datastatus) values('"""+str(utc)+"""',"""+str(latt)+""","""+str(lonn)+""","""+str(speed)+""",'"""+str(datastatus)+"""');"""
        return query

    def par_gll(self,line):
        data=[]
        data=line.split(',')

        utc=data[5][:2]+':'+data[5][2:4]+':'+data[5][4:6]

        if data[2]=='N':
            latt=float(data[1][:2])+float(data[1][2:])/60
        elif data[2]=='S':
            latt=-1*float(data[1][:2])+float(data[1][2:])/60
        else:
            latt=''

        ind=string.find(data[3],".")
        if data[4]=='E':
            lonn=float(data[3][:(ind-2)])+float(data[3][(ind-2):])/60
        elif data[4]=='W':
            lonn=-1*float(data[3][:(ind-2)])+float(data[3][(ind-2):])/60
        else:
            lonn=''

        if data[6]=='A':    datastatus=1
        else:   datastatus=0

        query="""insert into nmeaGLL(utcgll,latgll,longll,datastatus) values('"""+str(utc)+"""',"""+str(latt)+""","""+str(lonn)+""",'"""+str(datastatus)+"""');"""
        return query




