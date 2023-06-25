# learning-task-cloudbuild
Esempio di codice che, dopo la creazione di un Repository su Cloud Source Repository, tramite il deploy (pull request) di un codice basico (hello world) triggera il servizio Google Cloud Build che esegue una build (nell'esempio 2 step di esempio)

Per creare un repository:

1. Andare sulla Console GCP ed accedere al servizio Cloud Source Repository;
2. Cliccare su aggiungi repository in alto a destra e scegliere tra le due opzioni la più consona:
  2.1  Crea nuovo repository: creerà un repository vuoto non collegato a nessun servizio di hosting;
  2.2  Connetti repository esterno: permette di eseguire il mirroring di un repository da un servizio di hosting (GitHub) --> Se si sceglie questa opzione bisognerà prima creare un repository su Github in modo da poterlo collegare in fase di creazione;

3. Una volta creato il repository bisogna clonarsi il progetto, qui il clone del progetto tramite autenticazione SSH:
					3.1 In genere le chiavi SSH si trovano nella cartella ~/.ssh, per trovare sul proprio pc si può usare questo comando:
   								ls -a ~/.ssh
					3.2 Per prima cosa se non si hanno già sulla macchina bisognerà crearsi le chiavi SSH tramite il comando:
								ssh-keygen -t rsa -C "user@example.com"
					3.3 Una volta creata, va registrata sul proprio account dentro Cloud Source Repository;
					3.4 Successivamente si può clonare il repository:
								git clone ssh:[LINK DATO DA SOURCE CLOUD REPOSITORY]
					3.5 dopo essere stato clonato si deve passare al nuovo repository locale:
								cd [REPOSITORY LOCALE]
					3.6 Si devono creare i branch dev e test ed effettuare il primo push con entrambi:
								git checkout -b "dev"
								git checkout -b "test"

4. Tornando su Source Cloud Repository, andando sulle impostazioni del nostro repository possiamo trovare una voce TRIGGER DI CLOUD BUILD che ci rimanderà al servizio Cloud Build, qui possiamo entrare nella sezione dedicata ai trigger, cliccare su CREA TRIGGER ed inserire le configurazioni desiderate.

5.  Per far funzionare in maniera corretta Cloud Build, bisogna creare un file di configurazione YAML/JSON che conterrà le istruzioni per l'esecuzione delle attività in Cloud Build in base alle tue specifiche.
6.  Dopo aver creato questo file si può eseguire una push/pull request/merge request sul MAIN branch per far partire in maniera automatica la build con le istruzioni definite nel file YAML/JSON.
