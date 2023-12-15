import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string

nltk.download('punkt')
nltk.download('stopwords')


def summarize_text(text, num_sentences=5):
    #tokenizar oraciones y palabras
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    #preprocesamiento -> palabras de parada, signos de puntuacion y se asigna minuscula
    stop_words = set(stopwords.words('spanish') + list(string.punctuation))
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    #distribucion de frecuencia de palabras
    freq_dist = FreqDist(filtered_words)

    #puntajes para cada oración basándose en la frecuencia de las palabras en esa oración y ordenar segun puntaje
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in freq_dist.items():
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq
                else:
                    sentence_scores[sentence] = freq
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    selected_sentences = [sentence for sentence, score in sorted_sentences[:num_sentences]]

    #agregar a resumen en el orden original oraciones con mas score, no superando el limite de palabras
    countWord = 0
    ordered_summary = ''
    for sentence in sentences:
        if sentence in selected_sentences:
            splitedSentence = sentence.split()
            countWord += len(splitedSentence)
            if countWord < 100:
                ordered_summary += sentence + ' '

    return ordered_summary
