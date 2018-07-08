import os
import sys

def GeneralPurposeResister(p,q,r,s,t):
    A = [p,q,r,s,t]
    p= "".join(map(str, A))
    q= int(p, base=2)
    OutputFile.write ("R%d  "%q)

def Load_Store(p,q,r,s,t):
    A = [p,q,r,s,t]
    p= "".join(map(str, A))
    q= int(p, base=2)
    OutputFile.write ("(R%d)"%q)

def ForJump(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
    A = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    p= "".join(map(str, A))
    q= int(p, base=2)
    OutputFile.write ("#%d"%q)

def offset(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    L = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
    M = "".join(map(str, L))
    N= int(M, base=2)
    if p == 0:
        OutputFile.write ("#%d  "%N)
    else:
        X = ~N
        Y = 65537+X
        OutputFile.write ("#-%d  "%Y)

InputFile = None
OutputFile = None
Bit_Strings = []
Start_add = 496
try:
    InputFile = open('INPUT.txt')
    OutputFile = open('OUTPUT.txt', "w")
    for Bit_String in InputFile:
        if Bit_String.strip():
            Bit_Strings.append(Bit_String)

            for j in range(0,6):
                 OutputFile.write(Bit_String[j])
            OutputFile.write(' ')
            for j in range(6,11):
                 OutputFile.write(Bit_String[j])
            OutputFile.write(' ')
            for j in range(11,16):
                 OutputFile.write(Bit_String[j])
            OutputFile.write(' ')
            for j in range(16,21):
                 OutputFile.write(Bit_String[j])
            OutputFile.write(' ')
            for j in range(21,26):
                 OutputFile.write(Bit_String[j])
            OutputFile.write(' ')
            for j in range(26,32):
                 OutputFile.write(Bit_String[j])
            OutputFile.write('\t')
            OutputFile.write("%d"%Start_add)
            Start_add = Start_add + 4
            OutputFile.write('\t')

        if int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==0 \
                and int(Bit_String[6])==0 and int(Bit_String[7])==0 and int(Bit_String[8])==0 and int(Bit_String[9])==0 and int(Bit_String[10])==0 \
                and int(Bit_String[11])==0 and int(Bit_String[12])==0 and int(Bit_String[13])==0 and int(Bit_String[14])==0 and int(Bit_String[15])==0 \
                and int(Bit_String[16])==0 and int(Bit_String[17])==0 and int(Bit_String[18])==0 and int(Bit_String[19])==0 and int(Bit_String[20])==0 \
                and int(Bit_String[26])==0 and int(Bit_String[27])==0 and int(Bit_String[28])==1 and int(Bit_String[29])==1 and int(Bit_String[30])==0 and int(Bit_String[31])==1 :
            OutputFile.write("BREAK  ")

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==0 \
                and int(Bit_String[11])==0 and int(Bit_String[12])==0 and int(Bit_String[13])==0 and int(Bit_String[14])==0 and int(Bit_String[15])==0 \
                and int(Bit_String[16])==0 and int(Bit_String[17])==0 and int(Bit_String[18])==0 and int(Bit_String[19])==0 and int(Bit_String[20])==0 \
                and int(Bit_String[26])==0 and int(Bit_String[27])==0 and int(Bit_String[28])==1 and int(Bit_String[29])==0 and int(Bit_String[30])==0 and int(Bit_String[31])==0 :
            OutputFile.write("JR   ")
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))


        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==0 \
                and int(Bit_String[6])==0 and int(Bit_String[7])==0 and int(Bit_String[8])==0 and int(Bit_String[9])==0 and int(Bit_String[10])==0 \
                and int(Bit_String[11])==0 and int(Bit_String[12])==0 and int(Bit_String[13])==0 and int(Bit_String[14])==0 and int(Bit_String[15])==0 \
                and int(Bit_String[16])==0 and int(Bit_String[17])==0 and int(Bit_String[18])==0 and int(Bit_String[19])==0 and int(Bit_String[20])==0 \
                and int(Bit_String[26])==0 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==0 and int(Bit_String[30])==0 and int(Bit_String[31])==0 :
            OutputFile.write("NOP  ")
            
        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==0 \
                and int(Bit_String[21])==0 and int(Bit_String[22])==0 and int(Bit_String[23])==0 and int(Bit_String[24])==0 and int(Bit_String[25])==0 :

             if int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==0 and int(Bit_String[30])==0 and int(Bit_String[31])==0 :
                OutputFile.write("ADD   ")
             elif int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==1 and int(Bit_String[29])==0 and int(Bit_String[30])==1 and int(Bit_String[31])==0 :
                OutputFile.write("SLT   ")
             elif int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==0 and int(Bit_String[30])==0 and int(Bit_String[31])==1 :
                OutputFile.write("ADDU  ")
             elif int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==0 and int(Bit_String[30])==1 and int(Bit_String[31])==0 :
                OutputFile.write("SUB   ")
             elif int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==0 and int(Bit_String[30])==1 and int(Bit_String[31])==1 :
                OutputFile.write("SUBU  ")
             elif int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==1 and int(Bit_String[30])==1 and int(Bit_String[31])==1 :
                OutputFile.write("NOR   ")
             elif int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==1 and int(Bit_String[30])==0 and int(Bit_String[31])==0 :
                OutputFile.write("AND   ")
             elif int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==1 and int(Bit_String[30])==0 and int(Bit_String[31])==1 :
                OutputFile.write("OR    ")
             elif int(Bit_String[26])==1 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==1 and int(Bit_String[30])==1 and int(Bit_String[31])==0 :
                OutputFile.write("XOR   ")
             

             GeneralPurposeResister(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]))
             GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
             GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==0 and int(Bit_String[6])==0 \
                and int(Bit_String[7])==0 and int(Bit_String[8])==0 and int(Bit_String[9])==0 and int(Bit_String[10])==0:

            if int(Bit_String[26])==0 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==0 and int(Bit_String[30])==0 and int(Bit_String[31])==0 :
                    OutputFile.write("SLL   ")
            elif int(Bit_String[26])==0 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==0 and int(Bit_String[30])==1 and int(Bit_String[31])==1 :
                    OutputFile.write("SRA   ")
            elif int(Bit_String[26])==0 and int(Bit_String[27])==0 and int(Bit_String[28])==0 and int(Bit_String[29])==0 and int(Bit_String[30])==1 and int(Bit_String[31])==0 :
                    OutputFile.write("SRL   ")


            GeneralPurposeResister(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]))
            GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))
            GeneralPurposeResister(int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]))


        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==1 and int(Bit_String[4])==1 and int(Bit_String[5])==0 \
                and int(Bit_String[11])==0 and int(Bit_String[12])==0 and int(Bit_String[13])==0 and int(Bit_String[14])==0 and int(Bit_String[15])==0 :
            OutputFile.write("BLEZ  ")
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==1 and int(Bit_String[4])==1 and int(Bit_String[5])==1 \
                and int(Bit_String[11])==0 and int(Bit_String[12])==0 and int(Bit_String[13])==0 and int(Bit_String[14])==0 and int(Bit_String[15])==0 :
            OutputFile.write("BGTZ  ")
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==1 \
                and int(Bit_String[11])==0 and int(Bit_String[12])==0 and int(Bit_String[13])==0 and int(Bit_String[14])==0 and int(Bit_String[15])==1 :
            OutputFile.write("BGEZ  ")
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==1 and int(Bit_String[4])==0 and int(Bit_String[5])==1:
            OutputFile.write("BNE   ")
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==1 and int(Bit_String[4])==0 and int(Bit_String[5])==0:
            OutputFile.write("BEQ   ")
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))
            
        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==1 \
                and int(Bit_String[11])==0 and int(Bit_String[12])==0 and int(Bit_String[13])==0 and int(Bit_String[14])==0 and int(Bit_String[15])==0:
            OutputFile.write("BLTZ  ")
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))
        elif int(Bit_String[0])==1 and int(Bit_String[1])==0 and int(Bit_String[2])==1 and int(Bit_String[3])==0 and int(Bit_String[4])==1 and int(Bit_String[5])==1:
            OutputFile.write("SW    ")
            GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))
            Load_Store(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==1 and int(Bit_String[5])==0:
            OutputFile.write("J     ")
            ForJump(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]),int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]),
                   int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==1 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==0:
            OutputFile.write("ADDI  ")
            GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))

        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==1 and int(Bit_String[3])==0 and int(Bit_String[4])==1 and int(Bit_String[5])==0:
            OutputFile.write("SLTI  ")
            GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))


        elif int(Bit_String[0])==0 and int(Bit_String[1])==0 and int(Bit_String[2])==1 and int(Bit_String[3])==0 and int(Bit_String[4])==0 and int(Bit_String[5])==1:
            OutputFile.write("ADDIU  ")
            GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))
            GeneralPurposeResister(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))

        elif int(Bit_String[0])==1 and int(Bit_String[1])==0 and int(Bit_String[2])==0 and int(Bit_String[3])==0 and int(Bit_String[4])==1 and int(Bit_String[5])==1:
            OutputFile.write("LW    ")
            GeneralPurposeResister(int(Bit_String[11]),int(Bit_String[12]),int(Bit_String[13]),int(Bit_String[14]),int(Bit_String[15]))
            offset(int(Bit_String[16]),int(Bit_String[17]),int(Bit_String[18]),int(Bit_String[19]),int(Bit_String[20]),int(Bit_String[21]),int(Bit_String[22]),int(Bit_String[23]),int(Bit_String[24]),int(Bit_String[25]),
                   int(Bit_String[26]),int(Bit_String[27]),int(Bit_String[28]),int(Bit_String[29]),int(Bit_String[30]),int(Bit_String[31]))
            Load_Store(int(Bit_String[6]),int(Bit_String[7]),int(Bit_String[8]),int(Bit_String[9]),int(Bit_String[10]))

        

        OutputFile.write("\n")

finally:
    if InputFile is not None:
       InputFile.close()
    if OutputFile is not None:
       OutputFile.close()
