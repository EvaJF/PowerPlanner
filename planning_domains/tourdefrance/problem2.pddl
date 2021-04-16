


(define (problem tourdunord)




 (:domain TdF)


 (:objects Lille Arras Beauvais Laon Amiens Peronne SaintQuentin Chauny Compiegne Valenciennes Lens - position)


 (:init


   ; Directed graph



(connected  Lille Lens)
(connected  Lille Valenciennes)
(connected  Lens Arras)
(connected  Lens Valenciennes)
(connected  Valenciennes SaintQuentin)
(connected  Valenciennes Arras)
(connected  Valenciennes Peronne)
(connected  Arras Peronne)
(connected  Arras Amiens)
(connected  SaintQuentin Chauny)
(connected  SaintQuentin Laon)
(connected  SaintQuentin Peronne)
(connected  Peronne Amiens)
(connected  Peronne Chauny)
(connected  Amiens Beauvais)
(connected  Amiens Compiegne)
(connected  Amiens Chauny)
(connected  Chauny Compiegne)
(connected  Chauny Laon)
(connected  Compiegne Beauvais)
(connected  Lens Lille)
(connected  Valenciennes Lille)
(connected  Arras Lens)
(connected  Valenciennes Lens)
(connected  SaintQuentin Valenciennes)
(connected  Arras Valenciennes)
(connected  Peronne Valenciennes)
(connected  Peronne Arras)
(connected  Amiens Arras)
(connected  Chauny SaintQuentin)
(connected  Laon SaintQuentin)
(connected  Peronne SaintQuentin)
(connected  Amiens Peronne)
(connected  Chauny Peronne)
(connected  Beauvais Amiens)
(connected  Compiegne Amiens)
(connected  Chauny Amiens)
(connected  Compiegne Chauny)
(connected  Laon Chauny)
(connected  Beauvais Compiegne)







(at Lille)
(visited Lille)


 )







 (:goal (and


   (at Beauvais)


   (visited Laon)
   (visited Amiens)
   (visited Arras)

 ))


)


