


(define (problem pb1)




 (:domain TdF)


 (:objects Paris Rennes Brest Lille Amiens Rouen Caen LeMans Chartres Reims Metz Nancy Strasbourg Mulhouse Besancon Dijon Auxerre Orleans Tours Nantes Poitiers Limoges ClermontFerrand Nevers Lyon SaintEtienne Annecy Grenoble Nice Marseille Montpellier Millau Perpignan Toulouse Pau Agen Biarritz Bordeaux LaRochelle Gap Troyes - position)


 (:init


   ; Directed graph


(connected Brest Rennes)
(connected Rennes Caen)
(connected Rennes LeMans)
(connected Rennes Nantes)
(connected Caen Rouen)
(connected Rouen Paris)
(connected Rouen Amiens)
(connected Amiens Lille)
(connected Amiens Paris)
(connected Amiens Reims)
(connected Reims Paris)
(connected Reims Troyes)
(connected Reims Nancy)
(connected Reims Metz)
(connected Reims Lille)
(connected Metz Nancy)
(connected Metz Strasbourg)
(connected Nancy Strasbourg)
(connected Strasbourg Mulhouse)
(connected Mulhouse Besancon)
(connected Besancon Dijon)
(connected Dijon Auxerre)
(connected Dijon Lyon)
(connected Auxerre Troyes)
(connected Auxerre Paris)
(connected Auxerre Orleans)
(connected Auxerre Nevers)
(connected Orleans Paris)
(connected Orleans Chartres)
(connected Orleans Tours)
(connected Chartres Paris)
(connected Chartres LeMans)
(connected LeMans Tours)
(connected Tours Poitiers)
(connected Nevers ClermontFerrand)
(connected Poitiers LaRochelle)
(connected LaRochelle Bordeaux)
(connected Nantes LaRochelle)
(connected Poitiers Nantes)
(connected Limoges Poitiers)
(connected ClermontFerrand Limoges)
(connected Agen Bordeaux)
(connected Biarritz Bordeaux)
(connected Pau Biarritz)
(connected Toulouse Pau)
(connected Toulouse Agen)
(connected Montpellier Toulouse)
(connected Montpellier Perpignan)
(connected Montpellier Marseille)
(connected Millau Montepellier)
(connected ClermontFerrand Millau)
(connected SaintEtienne ClermontFerrand)
(connected Lyon ClermontFerrand)
(connected Lyon SaintEtienne)
(connected Annecy Lyon)
(connected Grenoble Lyon)
(connected Grenoble Annecy)
(connected Gap Grenoble)
(connected Nice Gap)
(connected Nice Marseille)
(connected Rennes Brest)
(connected Caen Rennes)
(connected LeMans Rennes)
(connected Nantes Rennes)
(connected Rouen Caen)
(connected Paris Rouen)
(connected Amiens Rouen)
(connected Lille Amiens)
(connected Paris Amiens)
(connected Reims Amiens)
(connected Paris Reims)
(connected Troyes Reims)
(connected Nancy Reims)
(connected Metz Reims)
(connected Lille Reims)
(connected Nancy Metz)
(connected Strasbourg Metz)
(connected Strasbourg Nancy)
(connected Mulhouse Strasbourg)
(connected Besancon Mulhouse)
(connected Dijon Besancon)
(connected Auxerre Dijon)
(connected Lyon Dijon)
(connected Troyes Auxerre)
(connected Paris Auxerre)
(connected Orleans Auxerre)
(connected Nevers Auxerre)
(connected Paris Orleans)
(connected Chartres Orleans)
(connected Tours Orleans)
(connected Paris Chartres)
(connected LeMans Chartres)
(connected Tours LeMans)
(connected Poitiers Tours)
(connected ClermontFerrand Nevers)
(connected LaRochelle Poitiers)
(connected Bordeaux LaRochelle)
(connected LaRochelle Nantes)
(connected Nantes Poitiers)
(connected Poitiers Limoges)
(connected Limoges ClermontFerrand)
(connected Bordeaux Agen)
(connected Bordeaux Biarritz)
(connected Biarritz Pau)
(connected Pau Toulouse)
(connected Agen Toulouse)
(connected Toulouse Montpellier)
(connected Perpignan Montpellier)
(connected Marseille Montpellier)
(connected Montepellier Millau)
(connected Millau ClermontFerrand)
(connected ClermontFerrand SaintEtienne)
(connected ClermontFerrand Lyon)
(connected SaintEtienne Lyon)
(connected Lyon Annecy)
(connected Lyon Grenoble)
(connected Annecy Grenoble)
(connected Grenoble Gap)
(connected Gap Nice)
(connected Marseille Nice)



(at Brest)
(visited Brest)


 )







 (:goal (and


   (at Paris)


   (visited Grenoble)
   (visited Marseille)
   (visited ClermontFerrand)
   (visited Limoges)
   (visited Nevers)
   (visited Strasbourg)
   (visited Biarritz)

 ))


)


