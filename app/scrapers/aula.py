from .base import BaseScraper

class AulaScraper(BaseScraper):
    def parse(self, soup):

        # find name and price
        # can use default meta content
        name = self.get_meta_content(soup, "og:title")
        price = self.get_meta_content(soup, "og:price:amount")

        # if found
        if name and price:
            return (name, price)
        # otherwise continue
        if not name:
            tag = soup.find("h1", class_="m_product-title")
            if tag:
                name = tag.text.strip()
        if not price:
            price_tag = soup.select_one(".m-price-item--regular")
            if price_tag:
                price = price_tag.text.strip()
            if price:
                price = float(price.replace("$", "").replace(",", "").strip())
        
        if name and price:
            return (name, price)
        
        raise Exception("Failed to parse Aula product")
        