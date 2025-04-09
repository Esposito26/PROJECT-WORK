document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("feedbackModal");
    const downloadBtn = document.getElementById("downloadBtn");
    const downloadPdfBtn = document.getElementById("downloadPdfBtn");
    const closeBtn = document.getElementsByClassName("close")[0];
    const feedbackForm = document.getElementById("feedbackForm");

    // Scarica il PDF
   downloadPdfBtn.onclick = () => {
    window.location.href = "/static/Documento Esplicativo per il Fattore di Rischio.pdf";
};


    // Mostra la modale
    downloadBtn.onclick = function () {
        modal.style.display = "block";
    }

    // Chiudi la modale quando clicchi la X
    closeBtn.onclick = function () {
        modal.style.display = "none";
    }

    // Chiudi la modale quando clicchi fuori
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Invio del feedback via fetch POST (AJAX)
    feedbackForm.onsubmit = async function (event) {
        event.preventDefault();

        const formData = new FormData(feedbackForm);

        try {
            const response = await fetch("/submit_feedback", {
                method: "POST",
                body: formData
            });

            if (response.ok) {
                alert("Grazie per il tuo feedback!");
                modal.style.display = "none";
                feedbackForm.reset();
            } else {
                alert("Errore nell'invio del feedback. Riprova.");
            }
        } catch (error) {
            console.error("Errore:", error);
            alert("Errore di connessione. Riprova.");
        }
    };
});
