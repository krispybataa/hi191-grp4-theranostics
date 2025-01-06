document.addEventListener('DOMContentLoaded', function() {
    // Handle collapsible sections
    const sections = document.querySelectorAll('.screening-section');
    sections.forEach(section => {
        const header = section.querySelector('.screening-header');
        header.addEventListener('click', () => {
            section.classList.toggle('active');
        });
    });

    // Open the first section by default
    if (sections.length > 0) {
        sections[0].classList.add('active');
    }

    // Function to handle lesion status changes
    function handleLesionStatusChange(organType, scanType) {
        const statusElement = document.getElementById(`id_${scanType}_${organType}_lesion_status`);
        const locationElement = document.getElementById(`id_${scanType}_${organType}_location`);
        const suvElement = document.getElementById(`id_${scanType}_${organType}_suv`);
        const sizeElement = document.getElementById(`id_${scanType}_${organType}_size`);

        if (statusElement && locationElement && suvElement && sizeElement) {
            const isAbsent = statusElement.value === 'Absent';
            
            // Disable/enable and clear related fields
            [locationElement, suvElement, sizeElement].forEach(element => {
                element.disabled = isAbsent;
                if (isAbsent) {
                    element.value = '';
                    element.style.backgroundColor = '#f0f0f0';
                } else {
                    element.style.backgroundColor = '';
                }
            });
        }
    }

    // Add event listeners for all lesion status dropdowns
    const organs = ['prostate', 'lymph_node', 'bone', 'brain', 'lung', 'liver'];
    const scanTypes = ['gapsma', 'fdgpetct'];
    
    organs.forEach(organ => {
        scanTypes.forEach(scanType => {
            const statusElement = document.getElementById(`id_${scanType}_${organ}_lesion_status`);
            if (statusElement) {
                // Initial state setup
                handleLesionStatusChange(organ, scanType);
                
                // Add change event listener
                statusElement.addEventListener('change', () => {
                    handleLesionStatusChange(organ, scanType);
                });
            }
        });
    });
});
