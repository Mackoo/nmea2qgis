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
        query="""update nmea2GGA set lat="""+str(latt)+""",lon="""+str(lonn)+""",fixstatus="""+str(fixstatus)+""",numsv="""+str(numsv)+""",hdop="""+str(hdop)+""",msl="""+str(msl)+""",geoid="""+str(geoid)+""" where utc='"""+utc+"""';"""
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

        query="""update nmea2GGA set lat="""+str(latt)+""",lon="""+str(lonn)+""",speed="""+str(speed)+""",datastatus='"""+str(datastatus)+"""' where utc='"""+utc+"""';"""
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
        query="""update nmea2GGA set lat="""+str(latt)+""",lon="""+str(lonn)+""",datastatus='"""+str(datastatus)+"""' where utc='"""+utc+"""';"""
        return query