import { HeaderContainer, Logo } from "./Header.style";


const   Header = () => {
    return (
        <HeaderContainer>
            <div>
                <Logo src="/images/logo.png"/>
            </div>

            <p>Encontre o par perfeito!</p>
        </HeaderContainer>
    )
}

export default Header;