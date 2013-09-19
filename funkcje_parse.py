import string
class funkcje:
    def par_gga(self,line):
        data=[]
        data=line.split(',')
        key=data[1]
        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        latt=float(data[2][:2])+float(data[2][2:])/60
        ind=string.find(data[4],".")
        lonn=float(data[4][:(ind-2)])+float(data[4][(ind-2):])/60
        numsv=data[7]
        hdop=data[8]
        msl=data[9]
        geoid=data[11]
        fixstatus=data[6]
        query="""insert into nmeaGGA values('"""+str(utc)+"""',"""+str(latt)+""","""+str(lonn)+""","""+str(fixstatus)+""","""+str(numsv)+""","""+str(hdop)+""","""+str(msl)+""","""+str(geoid)+""");"""
        return query


    def par_rmc(self,line):
        data=[]
        data=line.split(',')
        key=data[1]
        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        latt=float(data[3][:2])+float(data[3][2:])/60
        ind=string.find(data[5],".")
        lonn=float(data[5][:(ind-2)])+float(data[5][(ind-2):])/60
        speed=data[7]
        datastatus=data[2]

        query="""insert into nmeaRMC values('"""+str(utc)+"""',"""+str(latt)+""","""+str(lonn)+""","""+str(speed)+""",'"""+str(datastatus)+"""');"""
        return query

    def par_gll(self,line):
        data=[]
        data=line.split(',')
        key=data[5]
        utc=data[5][:2]+':'+data[5][2:4]+':'+data[5][4:6]
        latt=float(data[1][:2])+float(data[1][2:])/60
        ind=string.find(data[3],".")
        lonn=float(data[3][:(ind-2)])+float(data[3][(ind-2):])/60
        datastatus=data[6]
        query="""insert into nmeaGLL values('"""+str(utc)+"""',"""+str(latt)+""","""+str(lonn)+""",'"""+str(datastatus)+"""');"""
        return query