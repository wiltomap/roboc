<strong>Projet 'roboc'</strong>

Exercice dans le cadre du cours Openclassrooms "Apprenez à programmer en Python" (fin du chapitre 3)
> https://openclassrooms.com/courses/apprenez-a-programmer-en-python

--

<b>CONSIGNES :</b>

<p>Votre mission est de concevoir et <strong>développer un petit jeu permettant de contrôler un robot dans un labyrinthe</strong>. Ce jeu devra être développé en console pour des raisons d'accessibilité. Je l'ai appelé... <em>Roboc</em>.</p>
<p>Le jeu est un labyrinthe formé d'<strong>obstacles</strong> : des murs qui sont tout simplement là pour vous ralentir, des portes qui peuvent être traversées et au moins un point par lequel on peut quitter le labyrinthe. Si le robot arrive sur ce point, la partie est considérée comme gagnée.</p>
<p>&nbsp;</p>
<h3>Contrôle du robot</h3>
<p>Le robot est contrôlable grâce à des commandes entrées au clavier. Il doit exister les commandes suivantes :</p>
<ul>
<li><em>Q</em> qui doit permettre de <strong>sauvegarder</strong> et <strong>quitter</strong> la partie en cours ;</li>
<li><em>N</em> qui demande au robot de se <strong>déplacer vers le nord</strong> (c'est-à-dire le haut de votre écran) ;</li>
<li><em>E</em> qui demande au robot de se <strong>déplacer vers l'est</strong> (c'est-à-dire la droite de votre écran) ;</li>
<li><em>S</em> qui demande au robot de se <strong>déplacer vers le sud</strong> (c'est-à-dire le bas de votre écran) ;</li>
<li><em>O</em> qui demande au robot de se <strong>déplacer vers l'ouest</strong> (c'est-à-dire la gauche de votre écran) ;</li>
<li>Chacune des directions ci-dessus suivies d'un nombre permet&nbsp;d'avancer de <strong>plusieurs cases</strong> (par exemple <em>E3</em> pour avancer de trois cases vers l'est).</li>
</ul>
<p>&nbsp;</p>
<h3>Affichage du labyrinthe</h3>
<p>Le labyrinthe est vu du dessus. Un symbole représente un obstacle ou votre propre robot. Vous pouvez vous référez à l'exemple ci-dessous pour voir quelques exemples de partie.</p>
<p>Pour reconnaître la nature des obstacles, on doit bien évidemment représenter chaque obstacle par un <strong>symbole différent</strong>. Sans quoi, difficile de différencier les murs des portes de sorties.</p>
<p>&nbsp;</p>
<h3>Fonctionnalités du jeu</h3>
<p>Le jeu doit :</p>
<ul>
<li><strong>Enregistrer automatiquement</strong> chaque partie à chaque coup pour permettre de les continuer plus tard ;</li>
<li><strong>Proposer plusieurs cartes</strong> faciles à éditer. Chacune des cartes disponibles se trouvera dans un fichier avec&nbsp;l'extension <em>txt</em> dans un dossier particulier. Il sera donc facile d'<strong>ajouter, supprimer ou modifier des cartes</strong>. Vous pourrez télécharger les cartes par défaut plus bas.</li>
</ul>
<p>&nbsp;</p>
<h3>Au lancement du programme</h3>
<p>La première chose à faire est de trouver les cartes existantes, conservées dans nos fichiers <em>txt</em>, de les charger et de vérifier qu'une partie n'était pas en cours. Si une partie est en cours, <strong>proposer de rejouer cette partie</strong> (consultez l'exemple de jeu plus bas).</p>
<p>Choisir une carte lance la partie. La même chose se produit si vous demandez à jouer une partie déjà existante, s'il en existe une. <strong>À chaque tour, le labyrinthe est réaffiché</strong> avec la position de chaque obstacle et la position du robot.</p>
<p>&nbsp;</p>
<h3>Vous serez notés sur :</h3>
<ul>
<li>Le fait d'arriver à <strong>développer les fonctionnalités de l'exercice</strong> : si l'on peut lancer votre programme et qu'il tourne sans modification, vous aurez la note maximale, peu importe le code source derrière ;</li>
<li>La <strong>lisibilité du code</strong> : votre code source doit être aussi agréable à lire que possible. Les noms de vos variables, fonctions, classes, modules doivent être cohérents. La présentation de votre code source ne suit pas une règle spécifique, mais elle doit être cohérente (si vous faite un choix de nommage dans un module, faites le même choix dans un autre) ;</li>
<li>Le <strong>découpage de votre projet</strong> : essayez de bien réfléchir à la façon dont vous découperez votre projet. Les fonctions, classes, modules et éventuellement packages formeront la structure de votre projet ;</li>
<li>La <strong>documentation de votre code</strong> : indiquez de temps&nbsp;en temps des commentaires et documentations (sous forme de docstring, pour vos classes et fonctions), afin de rendre votre code plus compréhensible pour quelqu'un qui le regarde ;</li>
<li>L'<strong>ouverture à l'amélioration</strong> : ce dernier point est donné quand votre code est aussi&nbsp;séparé que possible et permettrait sans difficulté des modifications, comme l'ajout d'autres obstacles dans le labyrinthe, l'utilisation de cartes 3D avec des escaliers pour circuler de niveau en niveau, l'utilisation d'un affichage graphique avec l'une des bibliothèques existantes, etc. Si votre code est bien hiérarchisé, l'amélioration est généralement plus simple. <strong>Notez bien que vous n'avez pas à coder ces fonctionnalités, juste à garder en tête que votre programme pourrait évoluer par la suite.</strong></li>
</ul>
<p>&nbsp;</p>
<h3>Exemples de retour</h3>
<p>Vous pourrez trouver ci-dessous&nbsp;ce qu'on pourrait voir en exécutant le programme. Notez que :</p>
<ul>
<li>Les symboles utilisés sont O pour un mur, . pour une porte (sur laquelle le robot peut passer), U pour la sortie et X pour le robot lui-même ;</li>
<li>Quand le robot passe une porte, elle devient invisible et s'affiche de nouveau quand le robot est passé ;</li>
<li>Le robot ne peut pas passer au travers des murs ;</li>
<li>L'exemple ci-dessous est un exemple de la carte <em>facile</em>.</li>
</ul>
<pre>python roboc.py<br>
Labyrinthes existants :
  1 - facile.
  2 - prison.<br>
Entrez un numéro de labyrinthe pour commencer à jouer : 1<br>
OOOOOOOOOO
O O    O O
O . OO   O
O O O   XO
O OOOO O.O
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO

&gt; s<br>
OOOOOOOOOO
O O    O O
O . OO   O
O O O    O
O OOOO OXO
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO

&gt; n<br>
OOOOOOOOOO
O O    O O
O . OO   O
O O O   XO
O OOOO O.O
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO

&gt; s2<br>
OOOOOOOOOO
O O    O O
O . OO   O
O O O    O
O OOOO OXO
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO

OOOOOOOOOO
O O    O O
O . OO   O
O O O    O
O OOOO O.O
O O O   XU
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO

&gt; e<br>
OOOOOOOOOO
O O    O O
O . OO   O
O O O    O
O OOOO O.O
O O O    X
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO

Félicitations ! Vous avez gagné !
</pre>
<p>&nbsp;</p>
<h3>Cartes proposées par défaut</h3>
<p>Vous pouvez téléchargez un fichier .zip&nbsp;que j'ai préparé,&nbsp;contenant certaines cartes par défaut. Ces fichiers txt doivent être lus par votre programme. Vous êtes libres de les modifier, d'en ajouter ou supprimer, tant que votre programme arrive à lire les fichiers de carte donnés par défaut.</p>
<p>Rendez-vous <a title="ici pour télécharger le fichier .zip contenant les exemples de carte" href="https://static.oc-static.com/prod/courses/files/apprenez-a-programmer-en-python/Certification%20Python%20-%20partie%20III%20-%20cartes.zip">ici&nbsp;pour télécharger le fichier .<em>zip</em> contenant les exemples de carte</a>.</p>
<p>&nbsp;</p>
<h3>Code de base</h3>
<p>L'exercice peut sembler assez compliqué, même s'il s'agit d'un jeu plutôt&nbsp;basique. Je vous propose néanmoins une <strong>base de code</strong> avec certaines fonctionnalitées déjà implémentées, comme la lecture de carte. Vous n'êtes pas obligé de l'utiliser, mais cela pourra vous faire gagner du temps ! Rendez-vous <a href="https://static.oc-static.com/prod/courses/files/apprenez-a-programmer-en-python/Certification%20Python%20-%20partie%20III%20-%20code%20de%20base.zip">par ici pour télécharger le code de base</a>.</p>
<p>&nbsp;</p>
<h3>À inclure dans votre correction</h3>
<p>Vous devrez proposer en correction un fichier .<em>zip</em> qui devra contenir :</p>
<ul>
<li><strong>L'ensemble de votre code source</strong>. Le fichier à exécuter doit s'appeler <em>roboc.py</em> et doit se trouver à la racine de votre code source ;</li>
<li><strong>Une liste des cartes</strong> proposées par le programme. Le plus simple reste de créer un dossier <em>cartes</em> dans lequel se trouve les cartes. Là encore, le programme fourni doit être capable de les trouver sans modification du code.</li>
</ul>
<p>&nbsp;</p>
<p>À vous de jouer !&nbsp;</p>
    </div>
