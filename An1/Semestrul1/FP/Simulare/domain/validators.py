class ValidateImobil:
    def validare_imobil(self, imobil):
        """
        Verifica daca datele imobilului sunt corecte
        :param imobil: imobilul care se verifica
        :type imobil: Imobil
        """
        errors = []
        if imobil.get_id() < 0:
            errors.append('ID-ul imobilului trebuie sa fie un numar pozitiv.')
        if len(imobil.get_adresa()) < 2:
            errors.append('Adresa trebuie sa contina minim 2 caractere.')
        if imobil.get_pret() < 0:
            errors.append('Pretul dorit pe imobil nu poate sa fie negativ.')
        if imobil.get_tip() is not 'vanzare' or imobil.get_tip() is not 'inchiriere':
            errors.append('Tipul de oferta pentru imobilului introdus este gresit.')

        if len(errors) > 0:
            string_errors = '\n'.join(errors)
            return string_errors
