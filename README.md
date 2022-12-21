![HeaderML](header.jpg)

**Descripción**
-----------
El presente proyecto de machine learning tiene por objetivo la predicción del grado de daño de estructuras para el caso del terremoto del año 2015 sucedido en Nepal. 

Se intentaron diferentes modelos de machine learning y diferentes aproximaciones para ingeniería de variables, que podrán consultar en los notebooks, para finalmente quedarnos con el modelo que arrojaba las mejores métricas, el Catboost. El repo consta del procesamiento del dataset así como el entrenamiento de diferentes modelos. 


**Datos**
-----------

El dataset contiene datos relativos al terremoto de Nepal del año 2015. La recolección de los mismos llevada a cabo por el gobierno de dicho país, se hace con el propósito de determinar las personas que necesitarían ayudas gubernamentales para la reconstrucción de sus hogares. 

Por tanto, el dataset consta solo de edificios cuyo uso principal es la vivienda y algunos con usos secundarios. La encuesta principal consta de una serie de variables que fueron posteriormente purgadas para la competencia, dejando solo aquellas relacionadas con los edificios y el daño sufrido por los mismos. Contamos 156360 datos, constituidos por 38 atributos que describen diversos aspectos de cada edificio evaluado.

-----------
#### Fuentes de los Datos
* Extraído de Nepal Open Data Portal, https://eq2015.npc.gov.np/#/

#### Autores
* Génesis Rojas
