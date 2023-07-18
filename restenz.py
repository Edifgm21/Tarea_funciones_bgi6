def cortar_con_enzimas(seq, enzimas):
    """
    intput:
    ingreso de la secuencia
    enzimas:
    enzimas que ejecutan el corte en la secuencia
    output:
    secuencias cortadas

    """
    secuencias_cortadas = []    
    cortes = seq.split(enzimas)
    secuencias_cortadas.append(cortes)
    
    return secuencias_cortadas

