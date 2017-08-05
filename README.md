# REPO Publico :wheelchair: :wheelchair: :wheelchair: 

# Comandos
    # DESCARGAR ZIP
    >>>   curl -L -o master.zip http://github.com/pl4gue/master
    # DESCARGAR REPO
    >>>   git clone git@github.com:pl4gue/public.git
    >>>   git add .  #(en ./public )
    >>>   git commit -m "Comentario"
    >>>   git push   
  
# Entorno
    # Clave Pública
    >>>   //Crear clave
    >>>   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
                >>>   enter
                >>>   pass/pass
    >>>   //Iniciar agent segundo plano
    >>>   eval "$(ssh-agent -s)"
    >>>   //Añadir tu clave al ssh-Agent
    >>>   ssh-add ~/.ssh/id_rsa
    >>>   //Copiar en portapapeles la clave publica (~/.ssh/id_rsa.pub)
    >>>   //Dentro de GitHub :  Settings >> SSH and GPG >> Add New
    >>>   //Probar conexion
    >>>   ssh -T git@github.com
    
      
    
![image](command.png)
