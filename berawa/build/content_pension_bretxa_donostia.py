# Contenido de la demo Pensión Bretxa (Donostia-San Sebastián) (es/en/fr/de). Hechos de pensionbretxa.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Individual y doble','Doble familiar (3 camas)'],'en':['Single and double','Family double (3 beds)'],'fr':['Individuelle et double','Double familiale (3 lits)'],'de':['Einzel- und Doppelzimmer','Familien-Doppelzimmer (3 Betten)']}
RD={
'es':['Para quien viaja solo o en pareja, en el corazón de la Parte Vieja. Habitaciones insonorizadas con TV, calefacción y WiFi libre.','Para familias que buscan comodidad y cercanía, perfecta para disfrutar juntos de la Parte Vieja. Con TV, calefacción y WiFi libre.'],
'en':['For solo travellers or couples, in the heart of the Old Town. Soundproofed rooms with TV, heating and free WiFi.','For families looking for comfort and closeness, perfect for enjoying the Old Town together. With TV, heating and free WiFi.'],
'fr':['Pour voyager seul ou à deux, au cœur de la Vieille Ville. Chambres insonorisées avec TV, chauffage et WiFi libre.','Pour les familles qui cherchent confort et proximité, idéale pour profiter ensemble de la Vieille Ville. Avec TV, chauffage et WiFi libre.'],
'de':['Für Alleinreisende oder Paare, im Herzen der Altstadt. Schallisolierte Zimmer mit Fernseher, Heizung und freiem WLAN.','Für Familien, die Komfort und Nähe suchen, ideal, um gemeinsam die Altstadt zu genießen. Mit Fernseher, Heizung und freiem WLAN.']}
ART={
'hero':('waves',9601,['#e8eef1','#f5f2ec','#1d4e5f','#143846','#0b222b']),
'intro':('arches',9602,['#eef0ec','#e7b57f','#1d4e5f','#143846','#0b222b']),
'r1':('skyline',9611,['#143846','#e6a96b','#f4d6a7','#8a4b2c','#6f3c23','#472616']),
'r2':('hills',9612,['#e9eff0','#f1e6d0','#e5b474','#94b6b4','#628f8d','#406a68']),
'g1':('waves',9621,['#1d4e5f','#edbf87','#f6dfb7','#2c6a7e','#1d4e5f','#10303b']),
'g2':('columns',9622,['#edeae2','#f7f4ee','#8a4b2c','#143846','#0b222b']),
'g3':('arches',9623,['#ecdfca','#ddac76','#8a4b2c','#143846','#0b222b']),
'g4':('skyline',9624,['#143846','#e0a064','#f2cf9c','#7f4529','#683820','#432414'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Pensión Bretxa · Habitaciones en la Parte Vieja de Donostia',see_rooms='Ver las habitaciones',hero_k='Donostia-San Sebastián · Parte Vieja',hero_t='Habitaciones en la Parte Vieja de Donostia',hero_s='Para familias, parejas o «viajeros solitarios», a unos pasos de los bares de pintxos.',
 intro_t='Como en casa, fuera de casa',intro_p1='Pensión inaugurada en el año 2000 en la calle Fermín Calbetón, en pleno centro. «¡No vendemos camas!»: recomendaciones de ocio y cultura basadas en su experiencia.',
 intro_p2='La Parte Vieja es zona peatonal: hay dos parkings privados muy cercanos, en la Avenida del Boulevard y en la calle Okendo.',
 stats=['Desde el año 2000','Habitaciones insonorizadas','WiFi libre','Ascensor'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Individual, doble y doble familiar con 3 camas.',
 svcs=['TV en todas las habitaciones','Calefacción','WiFi libre','Lavadora para clientes','Ascensor','Recomendaciones de ocio y cultura'],
 around_s='A 5 minutos a pie: el Kursaal, el puerto y el Aquarium, la playa de La Concha. Ideal para peregrinos del Camino de Santiago.',
 loc_p='C/ Fermín Calbetón 5-2º · 20003 Donostia-San Sebastián, en la Parte Vieja.',
 chips=['¿Qué habitaciones tenéis?','¿Cuánto cuesta una habitación?','¿Dónde puedo aparcar?','¿Cómo reservo?']),
'en':dict(title='Pensión Bretxa · Rooms in the Old Town of Donostia',see_rooms='See the rooms',hero_k='Donostia-San Sebastián · Old Town',hero_t='Rooms in the Old Town of Donostia',hero_s='For families, couples or solo travellers, a few steps from the pintxos bars.',
 intro_t='A home away from home',intro_p1='A guesthouse opened in 2000 on Fermín Calbetón street, right in the centre. "We don\'t just sell beds!": leisure and culture tips based on their own experience.',
 intro_p2='The Old Town is pedestrian: there are two private car parks very close by, on Avenida del Boulevard and on Okendo street.',
 stats=['Since 2000','Soundproofed rooms','Free WiFi','Lift'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Single, double and family double with 3 beds.',
 svcs=['TV in every room','Heating','Free WiFi','Washing machine for guests','Lift','Leisure and culture tips'],
 around_s='A 5-minute walk: the Kursaal, the harbour and the Aquarium, La Concha beach. Ideal for Camino de Santiago pilgrims.',
 loc_p='C/ Fermín Calbetón 5-2º · 20003 Donostia-San Sebastián, in the Old Town.',
 chips=['Which rooms do you have?','How much is a room?','Where can I leave the car?','How do I book?']),
'fr':dict(title='Pensión Bretxa · Chambres dans la Vieille Ville de Donostia',see_rooms='Voir les chambres',hero_k='Donostia-San Sebastián · Vieille Ville',hero_t='Des chambres dans la Vieille Ville de Donostia',hero_s='Pour les familles, les couples ou les voyageurs solitaires, à deux pas des bars à pintxos.',
 intro_t='Comme à la maison, loin de chez soi',intro_p1='Pension ouverte en 2000 rue Fermín Calbetón, en plein centre. « Nous ne vendons pas que des lits ! » : conseils loisirs et culture tirés de leur expérience.',
 intro_p2='La Vieille Ville est piétonne : deux parkings privés tout proches, sur l\'Avenida del Boulevard et dans la rue Okendo.',
 stats=['Depuis 2000','Chambres insonorisées','WiFi libre','Ascenseur'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Individuelle, double et double familiale à 3 lits.',
 svcs=['TV dans toutes les chambres','Chauffage','WiFi libre','Lave-linge pour les clients','Ascenseur','Conseils loisirs et culture'],
 around_s='À 5 minutes à pied : le Kursaal, le port et l\'Aquarium, la plage de La Concha. Idéal pour les pèlerins du Chemin de Saint-Jacques.',
 loc_p='C/ Fermín Calbetón 5-2º · 20003 Donostia-San Sebastián, dans la Vieille Ville.',
 chips=['Quelles chambres avez-vous ?','Combien coûte une chambre ?','Où laisser la voiture ?','Comment réserver ?']),
'de':dict(title='Pensión Bretxa · Zimmer in der Altstadt von Donostia',see_rooms='Zimmer ansehen',hero_k='Donostia-San Sebastián · Altstadt',hero_t='Zimmer in der Altstadt von Donostia',hero_s='Für Familien, Paare oder Alleinreisende, wenige Schritte von den Pintxos-Bars.',
 intro_t='Wie zu Hause, nur unterwegs',intro_p1='Eine im Jahr 2000 eröffnete Pension in der Calle Fermín Calbetón, mitten im Zentrum. „Wir verkaufen nicht nur Betten!": Freizeit- und Kulturtipps aus eigener Erfahrung.',
 intro_p2='Die Altstadt ist Fußgängerzone: Ganz in der Nähe gibt es zwei private Parkhäuser, an der Avenida del Boulevard und in der Calle Okendo.',
 stats=['Seit 2000','Schallisolierte Zimmer','Freies WLAN','Aufzug'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Einzel-, Doppel- und Familien-Doppelzimmer mit 3 Betten.',
 svcs=['Fernseher in allen Zimmern','Heizung','Freies WLAN','Waschmaschine für Gäste','Aufzug','Freizeit- und Kulturtipps'],
 around_s='5 Gehminuten: Kursaal, Hafen und Aquarium, Strand La Concha. Ideal für Pilger auf dem Jakobsweg.',
 loc_p='C/ Fermín Calbetón 5-2º · 20003 Donostia-San Sebastián, in der Altstadt.',
 chips=['Welche Zimmer gibt es?','Was kostet ein Zimmer?','Wo kann ich das Auto abstellen?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='info@pensionbretxa.com')
D=dict(name='Pensión Bretxa',ac='#143846',ac2='#8a4b2c',ac2_a11y='#6f3c23',book=BOOK,around=[],foot=FOOT,
 address='C/ Fermín Calbetón 5-2º · 20003 Donostia-San Sebastián',phones=['+34 943 430 470','+34 646 957 745'],emails=['info@pensionbretxa.com'],maps='Pensión Bretxa, Fermín Calbetón 5, Donostia-San Sebastián',t=T)
META=dict(repo='demo-pension-bretxa-donostia',name='Pensión Bretxa',legal_name='Pensión Bretxa (titular persona física, autónomo, según el aviso legal de su web)',registry_ids=['NIF de persona física publicado en el aviso legal de su web (no se copia en la demo)'],
 url='https://www.pensionbretxa.com/',domain='pensionbretxa.com',municipality='Donostia-San Sebastián',province='Gipuzkoa',sector='pensión familiar abierta en 2000 en la Parte Vieja de Donostia-San Sebastián',
 read_at='2026-10-30T07:17:13+01:00',created_at='2026-10-30T07:16:30+01:00',built_at='2026-10-30T07:30:00+01:00',audit_date='2026-10-30T06:52:00+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T12:47:43+01:00',url='https://www.google.com/maps/place/Pensi%C3%B3n+Bretxa/@43.3235,-1.9834,17z/data=!4m9!3m8!1s0xd51a54dd94a1673:0xfdc463df0e95ead3!5m2!4m1!1i2!8m2!3d43.3235!4d-1.9834!16s%2Fg%2F1tmpltz0'),
 book=dict(mode='mail',url='mailto:info@pensionbretxa.com',note='Su web no tiene motor de reservas: «Reservar» lleva al teléfono (+34 943 43 04 70) y la página de contacto pide escribir a info@pensionbretxa.com. La demo enlaza el correo y el teléfono reales y no construye ningún motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cuánto cuesta una habitación?','K02'),('¿Dónde puedo aparcar?','K03'),('¿Hay wifi?','K04'),('¿Tenéis ascensor?','K05'),('¿Cómo llego desde la estación de tren?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('Hago el Camino de Santiago, ¿es buen sitio?','K09'),('¿Hay desayuno?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('How much is a room?','K02'),('Where can I leave the car?','K03'),('Is there wifi?','K04'),('Do you have a lift?','K05'),('How do I get there from the train station?','K06'),('What is your address?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('I am walking the Camino de Santiago, is it a good place?','K09'),('Is there breakfast?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Combien coûte une chambre ?','K02'),('Où laisser la voiture ?','K03'),('Y a-t-il le wifi ?','K04'),('Avez-vous un ascenseur ?','K05'),('Comment venir depuis la gare ?','K06'),('Quelle est votre adresse ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Je fais le Chemin de Saint-Jacques, est-ce un bon endroit ?','K09'),('Y a-t-il un petit-déjeuner ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was kostet ein Zimmer?','K02'),('Wo kann ich das Auto abstellen?','K03'),('Gibt es WLAN?','K04'),('Gibt es einen Aufzug?','K05'),('Wie komme ich vom Bahnhof hin?','K06'),('Wie ist Ihre Adresse?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Ich gehe den Jakobsweg, ist das ein guter Ort?','K09'),('Gibt es Frühstück?',None),('Haben Sie ein Schwimmbad?',None)]}
