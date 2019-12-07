INITIAL = "initial"
UPLOADED = "uploaded"

VALIDATE = "validando"
VALIDATE_WITH_ERROR = "validado_com_erro"

PROCESSING = "processando"
PROCESSING_WITH_ERROR = "processado_com_erro"
PROCESSING_WITH_SUCCESS = "processado_com_sucesso"


STATUS = (
    (INITIAL, "Inicio"),
    (UPLOADED, "Arquivo enviado"),
    (PROCESSING, "Arquivo sendo processado"),
    (PROCESSING_WITH_ERROR, "Arquivo processado com erro"),
    (PROCESSING_WITH_SUCCESS, "Arquivo procesado com sucesso"),
)
