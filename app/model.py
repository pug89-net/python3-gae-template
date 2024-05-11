class Area:
    """地域情報を表現するクラスです"""

    def __init__(self, area_code, area_name) -> None:
        self.area_code = area_code
        self.area_name = area_name


class Prefecture:
    """都道府県情報を表示するクラスです"""

    def __init__(
        self, area_code: str, prefecture_code: str, prefecture_name: str
    ) -> None:
        self.area_code = area_code
        self.prefecture_code = prefecture_code
        self.prefecture_name = prefecture_name

    def get_prefectures() -> list:
        return prefectures


area_block = [
    Area(area_code="HO", area_name="北海道"),
    Area(area_code="TOU", area_name="東北"),
    Area(area_code="KAN", area_name="関東"),
    Area(area_code="CHB", area_name="中部"),
    Area(area_code="KIN", area_name="近畿"),
    Area(area_code="CHG", area_name="中国"),
    Area(area_code="SHI", area_name="四国"),
    Area(area_code="KYU", area_name="九州"),
]

prefectures = [
    Prefecture(area_code="HO", prefecture_code="JP-01", prefecture_name="北海道"),
    Prefecture(area_code="TOU", prefecture_code="JP-02", prefecture_name="青森県"),
    Prefecture(area_code="TOU", prefecture_code="JP-03", prefecture_name="岩手県"),
    Prefecture(area_code="TOU", prefecture_code="JP-04", prefecture_name="宮城県"),
    Prefecture(area_code="TOU", prefecture_code="JP-05", prefecture_name="秋田県"),
    Prefecture(area_code="TOU", prefecture_code="JP-06", prefecture_name="山形県"),
    Prefecture(area_code="TOU", prefecture_code="JP-07", prefecture_name="福島県"),
    Prefecture(area_code="KAN", prefecture_code="JP-08", prefecture_name="茨城県"),
    Prefecture(area_code="KAN", prefecture_code="JP-09", prefecture_name="栃木県"),
    Prefecture(area_code="KAN", prefecture_code="JP-10", prefecture_name="群馬県"),
    Prefecture(area_code="KAN", prefecture_code="JP-11", prefecture_name="埼玉県"),
    Prefecture(area_code="KAN", prefecture_code="JP-12", prefecture_name="千葉県"),
    Prefecture(area_code="KAN", prefecture_code="JP-13", prefecture_name="東京都"),
    Prefecture(area_code="KAN", prefecture_code="JP-14", prefecture_name="神奈川県"),
    Prefecture(area_code="CHB", prefecture_code="JP-15", prefecture_name="新潟県"),
    Prefecture(area_code="CHB", prefecture_code="JP-16", prefecture_name="富山県"),
    Prefecture(area_code="CHB", prefecture_code="JP-17", prefecture_name="石川県"),
    Prefecture(area_code="CHB", prefecture_code="JP-18", prefecture_name="福井県"),
    Prefecture(area_code="CHB", prefecture_code="JP-19", prefecture_name="山梨県"),
    Prefecture(area_code="CHB", prefecture_code="JP-20", prefecture_name="長野県"),
    Prefecture(area_code="CHB", prefecture_code="JP-21", prefecture_name="岐阜県"),
    Prefecture(area_code="CHB", prefecture_code="JP-22", prefecture_name="静岡県"),
    Prefecture(area_code="CHB", prefecture_code="JP-23", prefecture_name="愛知県"),
    Prefecture(area_code="CHB", prefecture_code="JP-24", prefecture_name="三重県"),
    Prefecture(area_code="KIN", prefecture_code="JP-25", prefecture_name="滋賀県"),
    Prefecture(area_code="KIN", prefecture_code="JP-26", prefecture_name="京都府"),
    Prefecture(area_code="KIN", prefecture_code="JP-27", prefecture_name="大阪府"),
    Prefecture(area_code="KIN", prefecture_code="JP-28", prefecture_name="兵庫県"),
    Prefecture(area_code="KIN", prefecture_code="JP-29", prefecture_name="奈良県"),
    Prefecture(area_code="KIN", prefecture_code="JP-30", prefecture_name="和歌山県"),
    Prefecture(area_code="CHG", prefecture_code="JP-31", prefecture_name="鳥取県"),
    Prefecture(area_code="CHG", prefecture_code="JP-32", prefecture_name="島根県"),
    Prefecture(area_code="CHG", prefecture_code="JP-33", prefecture_name="岡山県"),
    Prefecture(area_code="CHG", prefecture_code="JP-34", prefecture_name="広島県"),
    Prefecture(area_code="CHG", prefecture_code="JP-35", prefecture_name="山口県"),
    Prefecture(area_code="SHI", prefecture_code="JP-36", prefecture_name="徳島県"),
    Prefecture(area_code="SHI", prefecture_code="JP-37", prefecture_name="香川県"),
    Prefecture(area_code="SHI", prefecture_code="JP-38", prefecture_name="愛媛県"),
    Prefecture(area_code="SHI", prefecture_code="JP-39", prefecture_name="高知県"),
    Prefecture(area_code="KYU", prefecture_code="JP-40", prefecture_name="福岡県"),
    Prefecture(area_code="KYU", prefecture_code="JP-41", prefecture_name="佐賀県"),
    Prefecture(area_code="KYU", prefecture_code="JP-42", prefecture_name="長崎県"),
    Prefecture(area_code="KYU", prefecture_code="JP-43", prefecture_name="熊本県"),
    Prefecture(area_code="KYU", prefecture_code="JP-44", prefecture_name="大分県"),
    Prefecture(area_code="KYU", prefecture_code="JP-45", prefecture_name="宮崎県"),
    Prefecture(area_code="KYU", prefecture_code="JP-46", prefecture_name="鹿児島県"),
    Prefecture(area_code="KYU", prefecture_code="JP-47", prefecture_name="沖縄県"),
]
