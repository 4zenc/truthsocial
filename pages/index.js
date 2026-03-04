import { createClient } from '@supabase/supabase-js';
import { useEffect, useState } from 'react';

const supabase = createClient('https://dbvnekxbwmpabjxcbjso.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRidm5la3hid21wYWJqeGNianNvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1Njk2MzgsImV4cCI6MjA4ODE0NTYzOH0.n92L0SDEOKDrk_r2DY-txXfft9hYKQWsXFVzolGGD98');

export default function Home() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    async function fetchNews() {
      const { data } = await supabase.from('news_items').select('*').order('created_at', { ascending: false });
      setNews(data);
    }
    fetchNews();
  }, []);

  return (
    <div style={{ minHeight: '100vh', background: '#050505', color: '#fff', padding: '40px 20px', fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif' }}>
      <header style={{ maxWidth: '600px', margin: '0 auto 40px' }}>
        <h1 style={{ fontSize: '2rem', letterSpacing: '-1px' }}>REALITY SNAPSHOT</h1>
        <p style={{ color: '#666' }}>No drama. No control. Just facts.</p>
      </header>

      <main style={{ maxWidth: '600px', margin: '0 auto' }}>
        {news.map((item) => (
          <article key={item.id} style={{ 
            background: 'rgba(255, 255, 255, 0.03)', 
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
            padding: '24px', 
            borderRadius: '16px',
            marginBottom: '20px'
          }}>
            <h2 style={{ fontSize: '1.25rem', marginBottom: '12px', lineHeight: '1.4' }}>{item.headline}</h2>
            <p style={{ color: '#aaa', fontSize: '0.95rem', marginBottom: '16px' }}>{item.impact}</p>
            <a href={item.source_url} target="_blank" style={{ color: '#fff', textDecoration: 'none', background: '#111', padding: '8px 16px', borderRadius: '8px', fontSize: '0.8rem', border: '1px solid #333' }}>
              VERIFY SOURCE
            </a>
          </article>
        ))}
      </main>
    </div>
  );
}