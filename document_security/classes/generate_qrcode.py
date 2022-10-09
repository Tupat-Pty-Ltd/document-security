import qrcode
import qrcode.image.svg


class DocumentQRCode:

    def __init__(self, document_url, qr_code_img_path):
        self.document_url = document_url

        # Contains path and file name with extention
        self.qr_code_img_path = qr_code_img_path

    def generate_qr_code(self):
        """Generates and returns a qr code image.
        """
        img = qrcode.make(
            self.document_url, image_factory=qrcode.image.svg.SvgImage)
        with open(self.qr_code_img_path, 'wb') as qr:
            img.save(qr)
        return self.qr_code_img_path