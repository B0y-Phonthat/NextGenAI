This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.


nextgen-ai/
├── backend/                # FastAPI Application
│   ├── app/
│   │   ├── api/            # API Endpoints (Routes)
│   │   │   ├── v1/         # Versioning สำหรับรองรับการอัปเดตในอนาคต
│   │   │   └── deps.py     # Dependencies (เช่น DB Session)
│   │   ├── core/           # Configuration & Security (Settings, .env)
│   │   ├── connect/         # Database (SQLAlchemy/SSMS)
│   │   ├── schemas/        # Pydantic Models (Data Validation) - ล้อกับ api.ts
│   │   ├── services/       # Business Logic Layer (ส่วนสำคัญที่สุด)
│   │   │   ├── storage.py  # จัดการ File System (Disk I/O)
│   │   │   └── training.py # จัดการ Queue และ Background Tasks
│   │   └── ml/             # AI/ML Engine (หัวใจของ AI Engineer)
│   │       ├── architecture/ # Custom Layers, Backbone Swapping
│   │       ├── engine/       # Training Loop, Inference Pipeline
│   │       └── utils/        # Image Processing (OpenCV), Augmentation
│   ├── storage/            # Local Storage สำหรับรูปภาพและ Weights (อยู่นอก app)
│   ├── .env                # เก็บ Connection String ของ SSMS
│   ├── requirements.txt
│   └── main.py             # Entry Point ของ Backend
├── frontend/               # Next.js Application (pnpm)
│   ├── src/
│   │   ├── app/            # Next.js App Router (Pages & Layouts)
│   │   ├── components/     # UI Components (HeroUI)
│   │   ├── services/       # API Client (ที่เก็บ api.ts ของคุณ)
│   │   ├── hooks/          # Custom React Hooks (เช่น useAnnotation)
│   │   └── types/          # TypeScript Interfaces (ที่ย้ายมาจาก api.ts)
│   ├── public/
│   └── package.json
└── .gitignore