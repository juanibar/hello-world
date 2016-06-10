import csv

#fileWriter: objeto csv.writer para armar el archivo de salida
#imgNum: posicion de la imagen actual en el archivo de test (de 1 a 28000)
#value: valor de la imagen actual que predijo la red neuronal (de 0 a 9)
def writeToSubmissionFile(fileWriter,imgNum, value):
	fileWriter.writerow([imgNum,value])


#--------------------debug------------------
subbmitWriter = csv.writer(open('submission.csv', 'a'))	#creo el writer
subbmitWriter.writerow(['ImageId','Label'])				#escribo la primer linea del archivo con los lavels
writeToSubmissionFile(subbmitWriter,2,3)				#escribo valores de prueba
writeToSubmissionFile(subbmitWriter,4,5)
writeToSubmissionFile(subbmitWriter,6,7)
writeToSubmissionFile(subbmitWriter,8,9)
del subbmitWriter										#elimino el writer