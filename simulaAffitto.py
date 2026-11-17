import streamlit as st
import pandas as pd

st.title("📈 Simulatore affitto")


#while i < 4:
   # i += 1
   # reddito_netto_atteso += 100
    #diminuzione_pc = (reddito_guadagnato - 100) / 100 * 60
  #  righe.append({
     #   "Iterazione": i,
     #   " reddito netto atteso": reddito_netto_atteso,
        #  qui devo aggiungere ....."Diminuzione %": diminuzione_pc,
   # })

#righe = []
#df = pd.DataFrame(righe)

#st.dataframe(df, use_container_width=True)



anniAmmortamento=10
tassoInteresse=10
reddito_netto_atteso = st.number_input("a quanto auspichi un reddito netto mensile per la Gianna?",  min_value=0, max_value=1800, step=1, )
costiRistrutturazione=st.number_input("a quanto prevedi i costi di ristrutturazione complessivi, DELL'APPARTAMENTO?", min_value=0,step=1)
anniAmmortamento=st.number_input("In quanti anni desideri l'ammortamento dei costi, PER L'APPARTAMENTO", min_value=1, max_value=100, step=1 ) #value=1.0,
debitoIpotecario=st.number_input("Quanto è il debito ipotecario RELATIVO SOLO ALL'APPARTAMENTO in questione?", min_value=0,step=1)
tassoInteresse=st.number_input("A quale tasso di interesse % ipotecario?")

affittoMensile=reddito_netto_atteso + (costiRistrutturazione/anniAmmortamento + debitoIpotecario*tassoInteresse/100)/12

st.write("l'affitto mensile AL NETTO DEI COSTI dovrà partire da Chf ", st.metric(affittoMensile, value="1.250", delta="+120")  #st.metric(label="Risultato", value="1.250", delta="+120")


#i = 0


#st.write("affittoMensile =",   affittoMensile, " >>> diminuzioneAnnualePc =", diminuzionePc)





#st.line_chart(
   # df.rename(columns={
        #"Iterazione": "iterazione",
        #"Reddito guadagnato": "reddito",
        #"Diminuzione %": "diminuzione",
   # }).set_index("iterazione")
#)

