


(define (problem touressonne)




 (:domain TdF)


 (:objects  Massy Gif Dourdan Angerville Etampes LaFerteAlais Evry Savigny - position)


 (:init


   ; Directed graph



(connected  Massy Gif)
(connected  Gif Dourdan)
(connected  Dourdan Angerville)
(connected  Dourdan Etampes)
(connected  Angerville Etampes)
(connected  Etampes LaFerteAlais)
(connected  LaFerteAlais Evry)
(connected  Evry Savigny)
(connected  Savigny Massy)
(connected  Gif Massy)
(connected  Dourdan Gif)
(connected  Angerville Dourdan)
(connected  Etampes Dourdan)
(connected  Etampes Angerville)
(connected  LaFerteAlais Etampes)
(connected  Evry LaFerteAlais)
(connected  Savigny Evry)
(connected  Massy Savigny)







(at Massy)
(visited Massy)


 )







 (:goal (and


   (at Angerville)
   (visited LaFerteAlais)



 ))


)


