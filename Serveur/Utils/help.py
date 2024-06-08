
def help() : 
    print("""
    Le serveur accepte les options suivantes : 
          -h/--help : affiche l'aide et les différentes options.
          -l/--listen <port> : se met en ecoute sue le port TCP saisi par l'utilisateur et attend lesdonnées du spiware.
          -s/--show : affiche tout la liste des fichiers réceptionnées par le programme.
          -r/--readfile <nom_fichier> : affiche le contenu du fichier stocké sur le serveur spiware.
          -k/--kill : arrête toute les instance de serveurs en cours, avertit le spyware de s'arreter et de supprimer la capture.
          -q/--quit : quitte le programme
    """)