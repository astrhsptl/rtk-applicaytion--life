import '../styles/register.css';

export default function Input({value, type, placeholderName, onChange}) {

    return(
        <input  
            class="input"
            value={value}
            type={type}
            placeholder={placeholderName}
            onChange={onChange}/>
    );
}