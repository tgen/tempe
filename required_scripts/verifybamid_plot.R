#!/usr/bin/env Rscript
library("optparse")
 
option_list = list(
  make_option(c("-i", "--input"), 
              type="character", 
              default=NULL, 
              help="dataset file name [required]"),
  make_option(c("-o", "--output"), 
              type="character", 
              default=NULL, 
              help="output prefix file name [required]"),
  make_option(c("-r", "--resources"), 
              type="character", 
              default=NULL, 
              help="path to VerifyBamID resource prefix [required]"),
  make_option(c("-t", "--type"), 
              type="character", 
              default="1000g", 
              help="refType to use (1000g, hgdp) [default= %default]"),
  make_option(c("-g", "--grey"), 
              type="logical", 
              default=FALSE, 
              help="plot reference panel sample as grey points [default= %default]")
);
 
opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

if (!is.null(opt$input)) {
  input <- opt$input
}
else {
  stop("-i/--input is required! See script usage (--help)")
}

if (!is.null(opt$output)) {
  output <- opt$output
}
else {
  stop("-o/--output is required! See script usage (--help)")
}

if (!is.null(opt$resources)) {
  resources <- opt$resources
}
else {
  stop("-r/--resources is required! See script usage (--help)")
}

type <- opt$type
isGrey <- opt$grey

#set background
library(ggplot2)
library(scales)
alphaScale=scale_alpha_discrete(range = c(0.9,0.3),guide=FALSE)
sizeScale=scale_size(range=c(1.5,1),guide=FALSE)
cat("Background data points:",type,"\n")
if(tolower(type)=="hgdp")
{
#set hgdp color scale
colScale = scale_color_manual(values=c('Adygei'='#00C6CD','Balochi'='#00FBFF','BantuKenya'='#FFB933','BantuSouthAfrica'='#FFB953','Basque'='#6495ED',
                                       'Bedouin'='#ADCE00','BiakaPygmy'='#CC9933','Brahui'='#CCE333','Burusho'='orchid4','Cambodian'='red',
                                       'Colombian'='#CC3333','Dai'='palevioletred4','Daur'='orangered2','Druze'='#00EEFF','French'='#0000FF','Han'='red4',
                                       'Han-NChina'='#CC7333','Hazara'='plum2','Hezhen'='#CCA333','Italian'='#00008B','Japanese'='#CC2333','Kalash'='purple4',
                                       'Karitiana'='#FF3D3D','Lahu'='#CC3A33','Makrani'='#339E00','Mandenka'='#FFB900','Maya'='#CC3333','MbutiPygmy'='#FFCD00',
                                       'Melanesian'='#CC3533','Miao'='#CC9333','Mongola'='#CC1333','Mozabite'='#ADCF00','Naxi'='orangered2','Orcadian'='#00EBFF',
                                       'Oroqen'='#ADCD00','Palestinian'='#00FBFF','Papuan'='darksalmon','Pathan'='purple','Pima'='#CC3333','Russian'='#00C6CD',
                                       'San'='#FFB953','Sardinian'='#00008B','She'='maroon','Sindhi'='#00EC20','Surui'='#CC3333','Tu'='maroon',
                                       'Tujia'='red3','Tuscan'='#00028B','Uygur'='#E11389','Xibo'='salmon','Yakut'='rosybrown1','Yi'='#CC3F33',
                                       'Yoruba'='#FFB933','UserSample'='#000000'),
                              breaks=c('Adygei','Balochi','BantuKenya','BantuSouthAfrica','Basque','Bedouin','BiakaPygmy','Brahui','Burusho','Cambodian',
                                       'Colombian','Dai','Daur','Druze','French','Han','Han-NChina','Hazara','Hezhen','Italian','Japanese','Kalash','Karitiana',
                                       'Lahu','Makrani','Mandenka','Maya','MbutiPygmy','Melanesian','Miao','Mongola','Mozabite','Naxi','Orcadian','Oroqen',
                                       'Palestinian','Papuan','Pathan','Pima','Russian','San','Sardinian','She','Sindhi','Surui','Tu','Tujia','Tuscan','Uygur',
                                       'Xibo','Yakut','Yi','Yoruba','UserSample'))
#set hgdp coordinates
POP=read.table(paste0(resources,"/hgdp.pop"), header = F)
RefCoord.hgdp=read.table(paste0(resources,".vcf.gz.dat.V"), header = F)
RefCoord.hgdp=RefCoord.hgdp[,1:3]
RefCoord.hgdp['POP'] <- POP$V2[match(RefCoord.hgdp$V1, POP$V1)]
colnames(RefCoord.hgdp)=c("ID","PC1","PC2","POP")
RefCoord=RefCoord.hgdp[!is.na(RefCoord.hgdp$POP),]
}else if(tolower(type)=="1000g"){
#set 1000g color scale
colScale = scale_color_manual(values=c('ESN'='#FFCD00','GWD'='#FFB900','LWK'='#CC9933','MSL'='#E1B919','YRI'='#FFB933','ACB'='#FF9900','ASW'='#FF6600',
                                       'CLM'='#CC3333','MXL'='#E10033','PEL'='#FF0000','PUR'='#CC3300','CDX'='#339900','CHB'='#ADCD00','CHS'='#00FF00',
                                       'JPT'='#008B00','KHV'='#00CC33','CEU'='#0000FF','FIN'='#00C5CD','GBR'='#00EBFF','IBS'='#6495ED','TSI'='#00008B',
                                       'BEB'='#8B008B','GIH'='#9400D3','ITU'='#B03060','PJL'='#E11289','STU'='#FF00FF','AFR'='#FFCD33','AFR/AMR'='#FF9900',
                                       'AMR'='#FF3D3D','EAS'='#ADFF33','EUR'='#64EBFF','SAS'='#FF30FF','UserSample'='#000000'),
                              breaks=c('ESN','GWD','LWK','MSL','YRI','ACB','ASW','CLM','MXL','PEL','PUR','CDX','CHB','CHS','JPT','KHV','CEU','FIN','GBR',
                                       'IBS','TSI','BEB','GIH','ITU','PJL','STU','AFR','AFR/AMR','AMR','EAS','EUR','SAS','UserSample'))
#set 1000g coordinates
POP=read.table(paste0(resources,"/1000g.pop"), header = F)
RefCoord.1kg=read.table(paste0(resources,".vcf.gz.dat.V"), header = F)
RefCoord.1kg=RefCoord.1kg[,1:3]
RefCoord.1kg['POP'] <- POP$V2[match(RefCoord.1kg$V1, POP$V1)]
colnames(RefCoord.1kg)=c("ID","PC1","PC2","POP")
RefCoord=RefCoord.1kg
}else
{
  stop("Argument 3 is required to be either 1000g or hgdp!\n")
}

#assuming the input target sample has format ID PC1 PC2
cat("Open file:",input,"\n")
TargetSample=read.table(file=input)
TargetSample=cbind(TargetSample,rep("UserSample",length(TargetSample$V1)))
colnames(TargetSample)=c("ID","PC1","PC2","POP")

if(isGrey)
{
cat("Background points color: grey\n")
#prepare dataset for plot
CombinedData=TargetSample
#plot RefCoord as grey
p=ggplot(data=RefCoord,aes(PC1,PC2))+geom_point(color="grey")+
  geom_point(data=CombinedData,aes(PC1,PC2,color=POP))+
  colScale+alphaScale+sizeScale
}else{
cat("Background points color: predefined color scale\n")
#prepare dataset for plot
CombinedData=rbind(RefCoord,TargetSample)
#plot RefCoord as colorful
p=ggplot()+geom_point(data=CombinedData,aes(PC1,PC2,color=POP))+#geom_text(data=CombinedData,aes(PC1,PC2,label=POP),size=1)+
  colScale+alphaScale+sizeScale
}

#ggsave(paste0(output,".pdf"))
pdf( paste0(output,".pdf"))
# Output all plots to currently active device
print( p )
# Close device
dev.off()