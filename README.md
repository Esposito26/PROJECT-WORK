# PROJECT WORK
**TITOLO:** 
Guida Pratica al Calcolo del Fattore di Rischio: Strumenti e Risorse per la Sicurezza sul Lavoro 

**Descrizione del Progetto**

Questo progetto è una semplice homepage che fornisce informazioni su un servizio di consulenza e prevenzione in materia di sicurezza sul lavoro. La pagina include dettagli sui servizi offerti, un documento scaricabile che spiega come calcolare il fattore di rischio e un modulo di feedback per raccogliere opinioni e suggerimenti dagli utenti.

**Struttura del Progetto**

File Principali

1. **index.html**                   # Il file HTML principale che definisce la struttura della homepage.
2. **style.css**                    # Il file CSS per la personalizzazione dello stile della pagina (non incluso nel codice fornito, ma indicato nel link).
3. **top logo-01.png**              # Logo utilizzato nella parte superiore della pagina.
4. **immagine consulenza.png** - Immagine principale utilizzata nella homepage.
5. **Documento Esplicativo per il Fattore di Rischio.pdf** - Documento scaricabile che illustra come calcolare il fattore di rischio.
6. **app.py**                       # Script principale per avviare il server Flask
7. **create_db**                    # Script per inizializzare il database e creare feedback.db
8. **feedback.db**                  # Database SQLite che memorizza i feedback degli utenti
9. **feedback.js**                  # Funzionalità JavaScript per la gestione della modale di feedback

Funzionalità

1. Download PDF
   Gli utenti possono scaricare gratuitamente un documento PDF informativo sulla sicurezza sul lavoro.
   Il pulsante "📄 Download PDF Gratis" avvia il download del PDF.

2. Modulo di Feedback
   Gli utenti possono inviare un feedback riguardo al PDF scaricato e alla navigazione del sito.
   Il modulo include domande sulla utilità del PDF, eventuali errori nel documento, valutazioni sul design del sito e suggerimenti per miglioramenti.
   Le risposte vengono inviate al backend tramite una richiesta POST.

3. Gestione dei Feedback
   I dati inviati attraverso il modulo di feedback vengono salvati nel database per una gestione successiva.

Il backend utilizza un database relazionale per conservare le informazioni sui feedback ricevuti, che possono essere utilizzati per migliorare i contenuti e la navigazione del sito.

**Istruzioni per l'Uso**

1. **Apri il file HTML**: Apri index.html con un browser web per visualizzare la homepage.
2. **Scarica il PDF**: Clicca sul pulsante "DOWNLOAD PDF GRATIS" per scaricare il documento.
3. **Invia Feedback**: Clicca sul pulsante "SCRIVI FEEDBACK" per aprire la modale e inviare il tuo feedback. Compila il modulo e invialo per ricevere un messaggio di conferma.

**Tecnologie Utilizzate**

1. Frontend (Client-Side)
  - **HTML5**: Per la struttura della pagina.
  - **CSS**: Per lo stile e il layout, inclusa la gestione di layout responsive e delle animazioni.
  - **JavaScript**: Per la funzionalità interattiva, inclusa la gestione della modale di feedback.
  - **Font Awesome**: Per le icone dei social media.

2. Backend (Server-Side)
  - **python**: Per linguaggio di programmazione principale utilizzato per lo sviluppo del backend.
  - **Flasck**: è un Micro-framework Python per la creazione e gestione delle rotte, la gestione dei file statici e la gestione delle richieste HTTP.

  - **Database**: Utilizzo di un database relazionale (come SQLite, PostgreSQL, ecc.) per memorizzare i dati inviati dagli utenti tramite il modulo di 
      feedback.

  - **Jinja2**: Motore di template di Flask utilizzato per il rendering dinamico delle pagine HTML e l'inclusione dei file statici (CSS, immagini, 
    JavaScript).


/Project Work
│
├── app.py                       # Script principale per avviare il server Flask
├── create_db                    # Script per inizializzare il database e creare feedback.db
├── feedback.db                  # Database SQLite che memorizza i feedback degli utenti
├── templates/
│   ├── index.html               # Pagina principale con il modulo di feedback e il download del PDF
│   ├── feedbacks.html           # Pagina per visualizzare tutti i feedback inviati
│   └── view_feedback.html       # Pagina per visualizzare un feedback specifico
│
├── static/
    ├── images/
    │   ├── top logo-01.png            # Logo della pagina
    │   └── immagine consulenza.png    # Immagine principale della homepage
    ├── Documento Esplicativo per il Fattore di Rischio.pdf      # PDF scaricabile
    ├── style.css                      # Stili generali per la pagina
    ├── feedback.css                   # Stili per il modulo di feedback
    └── js/
        └── feedback.js                # Funzionalità JavaScript per la gestione della modale di feedback



**Guida per lanciare il progetto localmente dal prompt dei comandi
Partiamo dal presupposto che tu abbia già Python e Flask installati.**
________________________________________
**1. Installa Python e Flask (se non già installati)**
Se non li hai già installati, apri il prompt dei comandi e digita:
	pip install python   

Attenzione: questo se il comando è errato, istalla Python da python.org
Poi installa Flask con:
	pip install flask
________________________________________
**2. Spostati nella cartella del progetto**
Apri il prompt dei comandi e spostati nella directory dove si trovano i file del tuo progetto:
	cd percorso/del/tuo/progetto
________________________________________
**3. Inizializza il database (solo la prima volta)**
Esegui lo script create_db.py per creare il file feedback.db:
	python create_db.py
________________________________________
**4. Avvia il server Flask**
Esegui lo script app.py per avviare il server locale:
	python app.py
Nel terminale vedrai un messaggio simile a:
	Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
________________________________________
**5. Apri il sito nel browser**
Vai nel tuo browser e apri:
	http://127.0.0.1:5000/ 
Questo caricherà il file index.html, servito da Flask.
________________________________________
**Ora puoi:**
•	 Visualizzare la homepage
•	Cliccare su “Download PDF Gratis” per scaricare il documento
•	Inviare un feedback tramite la modale (i dati verranno salvati in feedback.db)
________________________________________
**Altri percorsi utili**
•	http://127.0.0.1:5000/ → Carica index.html: homepage con download e modulo di feedback

•	http://127.0.0.1:5000/feedbacks.html → Carica feedbacks.html: elenco di tutti i feedback ricevuti

•	http://127.0.0.1:5000/view_feedback.html → Carica view_feedback.html: dettaglio dei singoli feedback memorizzati

Grazie.
