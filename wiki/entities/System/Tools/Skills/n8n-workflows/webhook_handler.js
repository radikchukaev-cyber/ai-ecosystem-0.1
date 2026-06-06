/**
 * n8n Webhook Handler
 * 
 * An Express.js middleware designed to intercept, format, and route 
 * incoming webhook requests to internal n8n instances or agent queues.
 */

const express = require('express');
const crypto = require('crypto');

const router = express.Router();
const SECRET_KEY = process.env.WEBHOOK_SECRET || 'default_dev_secret';

// Middleware to verify webhook signatures (e.g., from GitHub or Stripe)
function verifySignature(req, res, next) {
    const signature = req.headers['x-hub-signature-256'];
    if (!signature) {
        return res.status(401).json({ error: 'Missing signature header' });
    }

    const payload = JSON.stringify(req.body);
    const expectedSignature = `sha256=${crypto
        .createHmac('sha256', SECRET_KEY)
        .update(payload)
        .digest('hex')}`;

    if (crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expectedSignature))) {
        next();
    } else {
        res.status(403).json({ error: 'Invalid signature' });
    }
}

// Main webhook endpoint
router.post('/incoming', verifySignature, (req, res) => {
    const eventType = req.headers['x-event-type'] || 'unknown';
    const payload = req.body;
    
    console.log(`Received webhook event: ${eventType}`);
    
    // Normalize payload format before forwarding to n8n
    const normalizedData = {
        timestamp: new Date().toISOString(),
        source: req.ip,
        event: eventType,
        data: payload
    };
    
    // In a real implementation, this would forward to n8n via HTTP or message queue
    // forwardToN8n(normalizedData);
    
    res.status(202).json({ message: 'Webhook received and queued for processing.' });
});

module.exports = router;
