/**
 * Event handlers and listeners setup
 */

import { ELEMENTS } from './config.js';
import { qrManager } from './qr-manager.js';
import { themeManager } from './theme.js';
import { suggestionsManager } from './suggestions.js';
import { clearMessages, clearQROutput, debouncedClearQROutput } from './ui-utils.js';

/**
 * Setup all event listeners
 */
export function setupEventListeners() {
    const qrcodeInput = ELEMENTS.qrcodeInput;

    // Button handlers (no inline onclick, so the CSP can forbid inline scripts)
    ELEMENTS.themeToggle.addEventListener('click', () => themeManager.toggle());
    ELEMENTS.generateBtn.addEventListener('click', () => qrManager.generate());
    ELEMENTS.downloadBtn.addEventListener('click', () => qrManager.download());
    ELEMENTS.expandableHeader.addEventListener('click', () => suggestionsManager.toggle());
    
    // Add enter key support for input
    qrcodeInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            qrManager.generate();
        }
    });

    // Clear messages and QR output when user starts typing
    qrcodeInput.addEventListener('input', function() {
        clearMessages();
        debouncedClearQROutput(qrManager);
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + Enter to generate QR code
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            e.preventDefault();
            qrManager.generate();
        }
        
        // Escape to clear messages and QR output
        if (e.key === 'Escape') {
            clearMessages();
            clearQROutput(qrManager);
        }
    });
}