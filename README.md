# Plated by Benny - Website

A modern, responsive website for Plated by Benny, a gourmet dips and relishes brand that specializes in homemade, artisanal food products made with love.

## 🌟 Features

- **Modern Design**: Clean, professional layout with the brand's signature red and gold color scheme
- **Responsive**: Fully responsive design that works seamlessly on desktop, tablet, and mobile devices
- **Product Showcase**: Detailed product pages with ingredients, shelf life, and pricing information
- **Easy Navigation**: Intuitive navigation with smooth scrolling and mobile menu
- **Contact Integration**: WhatsApp and direct calling integration for easy ordering
- **Social Media Links**: Direct links to Instagram and WhatsApp
- **Professional About Page**: Brand story and values presentation

## 📁 Project Structure

```
platedbybenny/
├── index.html              # Landing page with featured products
├── products.html           # Full product catalog with filtering
├── about.html              # Brand story and information
├── css/
│   └── style.css          # Main stylesheet with responsive design
├── js/
│   └── script.js          # Interactive features and animations
├── assets/
│   ├── logo.svg           # Brand logo
│   ├── malabar-carrot.jpg # Product images (to be added)
│   ├── labneh-pearls.jpg
│   ├── honey-butter-blaze.jpg
│   ├── midnight-hummus.jpg
│   └── red-beret-salsa.jpg
└── README.md              # This file
```

## 🎨 Design System

### Color Palette
- **Primary Red**: `#C41E3A` - Main brand color
- **Dark Red**: `#8B1528` - Hover and emphasis states
- **Accent Gold**: `#D4AF37` - Highlights and accents
- **Light Gold**: `#F4E4C1` - Light backgrounds
- **Cream**: `#FAF8F3` - Page background

### Typography
- **Font Family**: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- **Heading Color**: Primary Red (#C41E3A)
- **Text Color**: Dark Gray (#333333)
- **Secondary Text**: Light Gray (#666666)

## 📱 Pages

### 1. **Home Page (index.html)**
- Hero section with call-to-action
- Featured product showcase
- Why choose Plated by Benny section
- How ordering works (4-step process)
- Contact information and social links

### 2. **Products Page (products.html)**
- Complete product catalog
- Filter by category (Dips, Spreads, Relishes)
- Detailed product cards with:
  - Product images
  - Price
  - Description
  - Ingredients
  - Weight and shelf life
  - Order buttons

### 3. **About Page (about.html)**
- Brand story and mission
- Core values
- Team/Founder information
- Production process
- Why choose Plated by Benny

## 🚀 Getting Started

### Prerequisites
- A web server (Apache, Nginx, etc.) or local development server
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd platedbybenny
   ```

2. **Serve locally** (using Python)
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Then visit http://localhost:8000
   ```

   Or using Node.js:
   ```bash
   npx http-server
   ```

3. **Add Product Images**
   Place the actual product images in the `assets/` folder:
   - `malabar-carrot.jpg`
   - `labneh-pearls.jpg`
   - `honey-butter-blaze.jpg`
   - `midnight-hummus.jpg`
   - `red-beret-salsa.jpg`

## 🔧 Customization

### Updating Content
- Edit HTML files directly to update product information, text, and links
- Modify color variables in `css/style.css` for brand color changes
- Update contact information in footer sections

### Adding Products
1. Add a new product card to `products.html`
2. Include product image in `assets/` folder
3. Update product details (price, ingredients, shelf life)

### Styling
- All CSS is contained in `css/style.css`
- CSS variables defined in `:root` for easy color/spacing modifications
- Mobile-first responsive design with media queries for tablets and phones

## 📲 Features

### Mobile Menu
- Hamburger menu appears on screens below 768px
- Smooth menu animations
- Auto-closes when navigation links are clicked

### Product Filtering
- Filter products by category on the products page
- Smooth transitions between filtered views

### Interactive Elements
- Animated navigation links with underline effect
- Product card hover effects
- Smooth scroll behavior
- Add to cart button feedback

### Contact Integration
- WhatsApp contact with pre-filled messages
- Phone number display
- Instagram links
- Social media icons

## 🛒 Ordering System

The website integrates with WhatsApp for order placement:
- Click "Order Now" or "WhatsApp" buttons
- Pre-filled messages with product information
- Direct WhatsApp chat for quick ordering
- Phone number: **9953118010**

## 📊 Product Information

### Available Products

1. **Malabar Spiced Carrot** - ₹229
   - Bold, tangy & aromatic carrot pickle
   - 180g | Shelf life: 1 month

2. **Labneh Pearls** - ₹299
   - Oregano & Chilli Flakes yogurt dip
   - 180g | Shelf life: 2 months

3. **Honey Butter Blaze** - ₹299
   - Sweet, savory & spicy butter spread
   - 180g | Shelf life: 2 months

4. **Midnight Hummus** - ₹229
   - Deep, creamy black chickpea dip
   - 180g | Shelf life: 14 days

5. **Red Beret Salsa** - ₹229
   - Smoky, zesty roasted tomato salsa
   - 180g | Shelf life: 7 days

## ✅ Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 License

This website is created for Plated by Benny. All rights reserved.

## 📧 Contact

For inquiries about the brand:
- **WhatsApp**: 9953118010
- **Instagram**: [@plated_by_benny](https://instagram.com/plated_by_benny)

## 🔄 Deployment

### Deploy to Web Host
1. Upload all files to your web hosting server
2. Ensure directory structure is maintained
3. Update any paths if hosting in a subdirectory
4. Test all links and functionality

### Popular Hosting Options
- Netlify (easy deployment from Git)
- Vercel
- GitHub Pages
- Traditional web hosting (Bluehost, GoDaddy, etc.)

## 🎯 Future Enhancements

- E-commerce integration for online payments
- Customer reviews and testimonials
- Blog section for recipes and food tips
- Email newsletter signup
- Multi-language support
- Customer account system
- Order tracking

---

**Version**: 1.0  
**Last Updated**: October 2024  
**Created with ❤️ for Plated by Benny**
