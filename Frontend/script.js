const API_BASE = 'http://127.0.0.1:8000';

async function fetchData(endpoint) {
    try {
        // Prevent browser caching by appending a timestamp and using no-store
        const url = new URL(`${API_BASE}${endpoint}`);
        url.searchParams.append('_t', new Date().getTime());
        
        const response = await fetch(url.toString(), { cache: 'no-store' });
        if (!response.ok) {
            alert(`Server Error (${response.status}) when fetching data. Check backend logs.`);
            return [];
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        alert('Network Error: Could not connect to the Django backend. Is the server running on port 8000?');
        return [];
    }
}

async function postData(endpoint, data, method = 'POST') {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (!response.ok) {
            alert(`Server Error (${response.status}) when saving data. Did you run the database migrations?`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error posting data:', error);
        alert('Network Error: Could not connect to the Django backend. Is the server running on port 8000?');
        return { error: 'Failed to save data' };
    }
}

function openModal(modalId) {
    document.getElementById(modalId).classList.add('active');
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
}

document.querySelectorAll('.close-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        this.closest('.modal').classList.remove('active');
    });
});
